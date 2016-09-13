from heppy.framework.analyzer import Analyzer
from heppy.papas.pfalgo.pfblockbuilder import PFBlockBuilder
from heppy.papas.data.pfevent import PFEvent
from heppy.papas.pfalgo.distance  import Distance


class PapasPFBlockBuilder(Analyzer):
    ''' Module to construct blocks of connected clusters and tracks 
        particles will eventually be reconstructed from elements of a block
        
        
        Usage:
        from heppy.analyzers.PapasPFBlockBuilder import PapasPFBlockBuilder
        pfblocks = cfg.Analyzer(
            PapasPFBlockBuilder,
            tracks = 'tracks', 
            ecals = 'ecal_clusters', 
            hcals = 'hcal_clusters', 
            history = 'history_nodes', 
            output_blocks = 'reconstruction_blocks'
        )
        
        tracks: Name of dict in Event where tracks are stored
        ecals: Name of dict in Event where ecals are stored
        hcals: Name of dict in Event where hcals are stored
        history: Name of history_nodes, can be set to None.
        output_blocks: Name to be used for the blocks dict
        
    '''
    def __init__(self, *args, **kwargs):
        super(PapasPFBlockBuilder, self).__init__(*args, **kwargs)
        
        self.tracksname = self.cfg_ana.tracks;    
        self.ecalsname = self.cfg_ana.ecals; 
        self.hcalsname = self.cfg_ana.hcals;
        self.blocksname = self.cfg_ana.output_blocks;
        self.historyname = self.cfg_ana.history;
        #self.outhistoryname = self.cfg_ana.outhistory;
        
                
    def process(self, event):
        
        pfevent=PFEvent(event) 
        
        distance = Distance()
        
        history_nodes =  None
        if hasattr(event, self.historyname) :
            history_nodes = getattr(event,  self.historyname)
        else:
            pass
        blockbuilder = PFBlockBuilder(pfevent, distance, history_nodes)
        #print blockbuilder
            
        setattr(event, "blocks", blockbuilder.blocks)
        #setattr(event, self.outhistoryname, blockbuilder.history_nodes)
        
        
        
