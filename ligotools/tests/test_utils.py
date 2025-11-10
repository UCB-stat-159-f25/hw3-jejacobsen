import numpy as np
from ligotools.utils import whiten, write_wavfile, reqshift

def test_whiten_preserves_length():
    """Test that whiten returns same length array as input"""
    # Create simple test data
    dt = 1.0/4096  # sampling interval
    N = 1000
    strain = np.random.randn(N)
    
    # Create a simple PSD function
    def simple_psd(f):
        return np.ones_like(f)
    
    # Test whiten
    whitened = whiten(strain, simple_psd, dt)
    
    assert len(whitened) == len(strain)
    assert isinstance(whitened, np.ndarray)

def test_reqshift_preserves_length():
    """Test that reqshift returns same length array as input"""
    # Create test data
    data = np.random.randn(1000)
    
    # Apply frequency shift
    shifted = reqshift(data, fshift=100, sample_rate=4096)
    
    # Check length is preserved
    assert len(shifted) == len(data)
    assert isinstance(shifted, np.ndarray)