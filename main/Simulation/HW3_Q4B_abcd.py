
from cc3d import CompuCellSetup
        

from HW3_Q4B_abcdSteppables import HW3_Q4B_abcdSteppable

CompuCellSetup.register_steppable(steppable=HW3_Q4B_abcdSteppable(frequency=1))


CompuCellSetup.run()
