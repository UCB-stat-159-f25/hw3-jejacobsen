import numpy as np
import ligotools.readligo as rl

def test_loaddata_returns_tuple():
    """Test that loaddata returns a tuple of three elements"""
    # Using one of the data files we moved to data/
    strain, time, chan_dict = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    
    # Check that we got three return values
    assert strain is not None
    assert time is not None
    assert chan_dict is not None
    
    # Check types
    assert isinstance(strain, np.ndarray)
    assert isinstance(time, np.ndarray)
    assert isinstance(chan_dict, dict)

def test_loaddata_strain_length():
    """Test that strain and time arrays have the same length"""
    strain, time, chan_dict = rl.loaddata('data/L-L1_LOSC_4_V2-1126259446-32.hdf5', 'L1')
    
    # Check that strain and time have the same length
    assert len(strain) == len(time)
    
    # Check that arrays are not empty
    assert len(strain) > 0
