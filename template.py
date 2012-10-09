init = '''
#define CF_MASK 1 << 1 // bit 1
#define PF_MASK 1 << 2 // bit 2
#define AF_MASK 1 << 4 // bit 4
#define ZF_MASK 1 << 6 // bit 6
#define SF_MASK 1 << 7 // bit 7
#define OF_MASK 1 << 11 // bit 11

'''
funcName = '''
static void Instrument_{0}(INS ins, void *v) {{
	%s
}}
'''

getMark = { "reg" : '''
  if(INS_OperandIsReg(ins, {0})) {{
    INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(TaintForRegister),
		   IARG_ADDRINT, INS_OperandReg(ins, {0}),
		   IARG_PTR, dest,
		   IARG_END);
  }}
  %s
		''',
			"mem" : '''
  if(INS_OperandIsMemory(ins, {0})) {{
    if(!INS_IsMemoryRead(ins)) return;
    INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(TaintForMemory),
		   IARG_MEMORYREAD_EA, IARG_MEMORYREAD_SIZE,
		   IARG_ADDRINT, INS_OperandMemoryBaseReg(ins, {0}),
		   IARG_ADDRINT, INS_OperandMemoryIndexReg(ins, {0}),
		   IARG_PTR, dest,
		   IARG_END);
  }}
  %s
  ''',

			"imm" : '''
	if(INS_OperandIsImmediate(ins, {0})) {{
	    INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(ClearTaintSet),
		   IARG_PTR, src,
		   IARG_END);
  }}
	%s
		''',
		"eflags"  : '''
	INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(TaintForRegister),
		 IARG_ADDRINT, LEVEL_BASE::REG_EFLAGS,
		 IARG_PTR, eflags,
		 IARG_END);
		%s
		'''
	}

setMark = { "reg" : '''
  if(INS_OperandIsReg(ins, {0})) {{
    INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(SetTaintForRegister),
		   IARG_ADDRINT, INS_OperandReg(ins, {0}),
           IARG_UINT32, 2,
		   IARG_PTR, dest,
		   IARG_PTR, src,
		   IARG_END);
  }}
  %s
  ''',
  		"mem" : '''
  if(INS_OperandIsMemory(ins, {0})) {{
    if(!INS_IsMemoryWrite(ins)) return;

    INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(SetTaintForMemory),
		   IARG_MEMORYWRITE_EA, IARG_MEMORYWRITE_SIZE,
		   IARG_UINT32, 2,
           IARG_PTR, dest,
		   IARG_PTR, src,
		   IARG_END);
  }}
  %s
  ''',
	"eflags" : '''
	INS_InsertCall(ins, IPOINT_BEFORE, AFUNPTR(SetTaintForRegister),
		 IARG_ADDRINT, LEVEL_BASE::REG_EFLAGS,
         IARG_UINT32, 2,
		 IARG_PTR, dest,
		 IARG_PTR, src,
		 IARG_END);
	%s
	'''

  	}


unknown = '''
  else {{
      log << "Unknown operand({0}) type: " << INS_Disassemble(ins) << "\\n";
      log.flush();
    abort();
  }}
  %s
  '''



if __name__ == "__main__":
	print getMark["reg"]
	print getMark["reg"].format(1)
