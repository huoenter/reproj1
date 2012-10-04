##Description##
Using JSON to represent the semantics of the taint mark propagation.
###tap###
Things will affect the propagation.
###sink###
Things will be affected.
###members for tap/sink###
The names are arbitary. Each has a type field that 
[imm, mem, reg] which can be number 1, 4, 5, 7 which indicates the types that
operand can be. ''pos'' stands for the position of the operand when called by
 Pin's API.
###operation###
Currently just indicates what the instruction does.
###dependency(to appear)###
If the taint marks will be propagated when encountering conditional instructions.
