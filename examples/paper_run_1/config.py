# General

# raw data paths

raw_data_dir = "../../data/Baltruschat/"
TRAIN_SIZE = 0.8

# Morgan fingerprints
FP_BITS = 4096
FP_RADIUS = 3

# Random Forest
NUM_ESTIMATORS = 100  # 1000 Baltruschat

# GCN
BATCH_SIZE = 64
LEARNING_RATE = 0.001
NUM_EPOCHS = 2000  # 3000

NUM_GRAPH_LAYERS = 4
NUM_LINEAR_LAYERS = 2
HIDDEN_CHANNELS = 96

list_node_features = [
    "atomic_number",
    "formal_charge",
    #     'chiral_tag',
    "hybridization",
    "total_num_Hs",
    #     'explicit_num_Hs',
    "aromatic_tag",
    "total_valence",
    "total_degree",
    "is_in_ring",
    #     'amide_center_atom'
]
list_edge_features = ["bond_type", "is_conjugated", "rotatable"]

num_node_features = len(list_node_features)
num_edge_features = len(list_edge_features)

