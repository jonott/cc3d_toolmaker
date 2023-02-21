
from cc3d.core.PySteppables import *


class HW3_Q4B_abcdSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        
        self.plot_win = self.add_new_plot_window(title='Light-Light and Light-Medium Contact Areas',
                                      x_axis_title='MonteCarlo Step (MCS)',
                                      y_axis_title='Contact', x_scale_type='linear', y_scale_type='linear',
                                      grid=True, config_options={'legend': True})
        
        self.plot_win.add_plot("LL", style='Dots', color='red', size=5)
        self.plot_win.add_plot("LM", style='Dots', color='orange', size=5)
        self.plot_win.add_plot("DD", style='Dots', color='yellow', size=5)
        self.plot_win.add_plot("DL", style='Dots', color='blue', size=5)
        self.plot_win.add_plot("DM", style='Dots', color='green', size=5)

    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """ 
        
        
        for cell in self.cell_list:

            print("cell.id=",cell.id)
            # arguments are (name of the data series, x, y)
            #self.plot_win.add_data_point("MVol", mcs, cell.volume)
            #self.plot_win.add_data_point("MSur", mcs, cell.surface)
            cell_neighbors = self.get_cell_neighbor_data_list(cell)
            CSA_LL = cell_neighbors.common_surface_area_with_cell_types([self.LIGHT, self.LIGHT])
            CSA_LM = cell_neighbors.common_surface_area_with_cell_types([self.LIGHT, self.MEDIUM])
            CSA_DD = cell_neighbors.common_surface_area_with_cell_types([self.DARK, self.DARK])
            CSA_DL = cell_neighbors.common_surface_area_with_cell_types([self.DARK, self.LIGHT]) 
            CSA_DM = cell_neighbors.common_surface_area_with_cell_types([self.DARK, self.MEDIUM])   
            self.plot_win.add_data_point("LL", mcs, CSA_LL)
            self.plot_win.add_data_point("LM", mcs, CSA_LM)        
            self.plot_win.add_data_point("DD", mcs, CSA_DD)
            self.plot_win.add_data_point("DL", mcs, CSA_DL)    
            self.plot_win.add_data_point("DM", mcs, CSA_DM)        

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
