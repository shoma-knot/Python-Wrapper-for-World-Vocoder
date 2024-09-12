import numpy as np
from typing import Optional

default_f0_ceil = 800.0
default_f0_floor = 71.0

default_frame_period = 5.0

def cheaptrick(
    x: np.ndarray,
    f0: np.ndarray,
    temporal_positions: np.ndarray,
    fs: int,
    q1: float = -0.15,
    f0_floor: Optional[float] = default_f0_floor,
    fft_size: Optional[int] = None,
) -> np.ndarray:
    """CheapTrick harmonic spectral envelope estimation algorithm.

    Args:
        x (np.ndarray): Input waveform signal.
        f0 (np.ndarray): Input F0 contour.
        temporal_positions (np.ndarray): Temporal positions of each frame.
        fs (int): Sample rate of input signal in Hz.
        q1 (float, optional): Spectral recovery parameter. Default to -0.15 (this value was tuned and normally does not need adjustment).
        f0_floor (Optional[float], optional): Lower F0 limit in Hz. Not used in case `fft_size` is specified. Defaults to default_f0_floor.
        fft_size (Optional[int], optional):
            FFT size to be used. When `None` (default) is used, the FFT size is computed automatically as a function of the given input sample rate and F0 floor.
            When `fft_size` is specified, the given `f0_floor` parameter is ignored. Defaults to None.

    Returns:
        np.ndarray: Spectral envelope (squared magnitude).
    """
    pass

def code_aperiodicity(aperiodicity: np.ndarray, fs: int) -> np.ndarray:
    """Reduce dimensionality of D4C aperiodicity.

    Args:
        aperiodicity (np.ndarray): Aperodicity envelope.
        fs (int): Sample rate of input signal in Hz.

    Returns:
        np.ndarray: Coded aperiodicity envelope.
    """
    pass

def code_spectral_envelope(
    spectrogram: np.ndarray,
    fs: int,
    number_of_dimensions: int,
) -> np.ndarray:
    """Reduce dimensionality of spectral envelope.

    Args:
        spectrogram (np.ndarray): Spectral envelope.
        fs (int): Sample rate of input signal in Hz.
        number_of_dimensions (int): Number of dimentions of coded spectral envelope

    Returns:
        np.ndarray: Coded spectral envelope.
    """
    pass

def d4c(
    x: np.ndarray,
    f0: np.ndarray,
    temporal_positions: np.ndarray,
    fs: int,
    q1: float = -0.15,
    threshold: float = 0.85,
    fft_size: Optional[float] = None,
) -> np.ndarray:
    """D4C aperiodicity estimation algorithm.

    Args:
        x (np.ndarray): Input waveform signal.
        f0 (np.ndarray): Input F0 contour.
        temporal_positions (np.ndarray): Temporal positions of each frame.
        fs (int): Sample rate of input signal in Hz.
        q1 (float, optional): Spectral recovery parameter. Defaults to -0.15 (this value was tuned and normally does not need adjustment).
        threshold (float, optional):
            Threshold for aperiodicity-based voiced/unvoiced decision, in range 0 to 1.
            If a value of 0 is used, voiced frames will be kept voiced. If a value > 0 is used some voiced frames can be considered unvoiced by setting their aperiodicity to 1 (thus synthesizing them with white noise).
            Using `threshold=0` will result in the behavior of older versions of D4C.
            The current default of 0.85 is meant to be used in combination with the Harvest F0 estimator, which was designed to have a high voiced/unvoiced threshold (i.e. most frames will be considered voiced). Defaults to 0.85.
        fft_size (Optional[float], optional):
            FFT size to be used. When `None` (default) is used, the FFT size is computed automatically as a function of the given input sample rate and the default F0 floor.
            When `fft_size` is specified, it should match the FFT size used to compute the spectral envelope (i.e. `fft_size=2*(sp.shape[1] - 1)`) in order to get the desired results when resynthesizing. Defaults to None.

    Returns:
        np.ndarray: Aperiodicity (envelope, linear magnitude relative to spectral envelope).
    """
    pass

def decode_aperiodicity(
    coded_aperiodicity: np.ndarray, fs: int, fft_size: int
) -> np.ndarray:
    """Restore full dimensionality of coded D4C aperiodicity.

    Args:
        coded_aperiodicity (np.ndarray): Coded aperodicity envelope.
        fs (int): Sample rate of input signal in Hz.
        fft_size (int): FFT size corresponding to the full dimensional aperiodicity.

    Returns:
        np.ndarray: Aperiodicity envelope.
    """
    pass

def decode_spectral_envelope(
    coded_spectral_envelope: np.ndarray, fs: int, fft_size: int
) -> np.ndarray:
    """Restore full dimensionality of coded spectral envelope.

    Args:
        coded_spectral_envelope (np.ndarray): Coded spectral envelope.
        fs (int): Sample rate of input signal in Hz.
        fft_size (int): FFT size corresponding to the full dimensional spectral envelope.

    Returns:
        np.ndarray: Spectral envelope.
    """
    pass

def dio(
    x: np.ndarray,
    fs: int,
    f0_floor: float = default_f0_floor,
    f0_ceil: float = default_f0_ceil,
    channels_in_octave: float = 2.0,
    frame_period: float = default_frame_period,
    speed: int = 1,
    allowed_range: float = 0.1,
) -> tuple[np.ndarray, np.ndarray]:
    """DIO F0 extraction algorithm.

    Args:
        x (np.ndarray): Input waveform signal.
        fs (int): Sample rate of input signal in Hz.
        f0_floor (float, optional): Lower F0 limit in Hz. Defaults to default_f0_floor.
        f0_ceil (float, optional): Upper F0 limit in Hz. Defaults to default_f0_ceil.
        channels_in_octave (float, optional): Resolution of multiband processing; normally shouldn't be changed. Defaults to 2.0.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.
        speed (int, optional):
            The F0 estimator may downsample the input signal using this integer factor (range [1;12]).
            The algorithm will then operate on a signal at fs/speed Hz to reduce computational complexity, but high values may negatively impact accuracy. Defaults to 1 (no downsampling).
        allowed_range (float, optional):
            Threshold for voiced/unvoiced decision.
            Can be any value >= 0, but 0.02 to 0.2 is a reasonable range.
            Lower values will cause more frames to be considered unvoiced (in the extreme case of `threshold=0`, almost all frames will be unvoiced). Defaults to 0.1.

    Returns:
        tuple[np.ndarray, np.ndarray]: Tuple of **estimated F0 contour** and **temporal position of each frame**.
    """
    pass

def get_cheaptrick_f0_floor(fs: int, fft_size: int) -> float:
    """Calculates actual lower F0 limit for CheapTrick based on the sampling frequency and FFT size used.
    Whenever F0 is below this threshold the spectrum will be analyzed as if the frame is unvoiced (using kDefaultF0 defined in constantnumbers.h).

    Args:
        fs (int): Sample rate of input signal in Hz.
        fft_size (int): FFT size used for CheapTrick.


    Returns:
        float: Resulting lower F0 limit in Hz.
    """
    pass

def get_cheaptrick_fft_size(fs: int, f0_floor: float = default_f0_floor) -> int:
    """Calculate suitable FFT size for CheapTrick given F0 floor.

    Args:
        fs (int): Sample rate of input signal in Hz.
        f0_floor (float, optional): Lower F0 limit in Hz. The required FFT size is a direct consequence of the F0 floor used. Defaults to default_f0_floor.

    Returns:
        int: Resulting FFT size.
    """

    pass

def get_num_aperiodicities(fs: int) -> int:
    """Calculate the required dimensionality to code D4C aperiodicity.

    Args:
        fs (int): Sample rate of input signal in Hz.

    Returns:
        int: Required number of coefficients.
    """
    pass

def harvest(
    x: np.ndarray,
    fs: int,
    f0_floor: float = default_f0_floor,
    f0_ceil: float = default_f0_ceil,
    frame_period: float = default_frame_period,
) -> tuple[np.ndarray, np.ndarray]:
    """Harvest F0 extraction algorithm.

    Args:
        x (np.ndarray): Input waveform signal.
        fs (int): Sample rate of input signal in Hz.
        f0_floor (float, optional): Lower F0 limit in Hz. Defaults to default_f0_floor.
        f0_ceil (float, optional): Upper F0 limit in Hz. Defaults to default_f0_ceil.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.

    Returns:
        tuple[np.ndarray, np.ndarray]: Tuple of **estimated F0 contour** and **temporal position of each frame**.
    """
    pass

def stonemask(
    x: np.ndarray, f0: np.ndarray, temporal_positions: np.ndarray, fs: int
) -> np.ndarray:
    """StoneMask F0 refinement algorithm.

    Args:
        x (np.ndarray): Input waveform signal.
        f0 (np.ndarray): Input F0 contour.
        temporal_positions (np.ndarray): Temporal positions of each frame.
        fs (int): Sample rate of input signal in Hz.

    Returns:
        np.ndarray: Refined F0 contour.
    """
    pass

def synthesize(
    f0: np.ndarray,
    spectrogram: np.ndarray,
    aperiodicity: np.ndarray,
    fs: int,
    frame_period: float = default_frame_period,
) -> np.ndarray:
    """WORLD synthesis from parametric representation.

    Args:
        f0 (np.ndarray): Input F0 contour.
        spectrogram (np.ndarray): Spectral envelope.
        aperiodicity (np.ndarray): Aperodicity envelope.
        fs (int): Sample rate of input signal in Hz.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.

    Returns:
        np.ndarray: Output waveform signal.
    """
    pass

def wav2world(
    x: np.ndarray, fs: int, fft_size: int, frame_period: float = default_frame_period
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convenience function to do all WORLD analysis steps in a single call.
    In this case only `frame_period` can be configured and other parameters are fixed to their defaults.
    Likewise, F0 estimation is fixed to DIO plus StoneMask refinement.

    Args:
        x (np.ndarray): Input waveform signal.
        fs (int): Sample rate of input signal in Hz.
        fft_size (int):
            Length of Fast Fourier Transform (in number of samples).
            The resulting dimension of `ap` adn `sp` will be `fft_size` // 2 + 1.
        frame_period (float, optional): Period between consecutive frames in milliseconds. Defaults to default_frame_period.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Tuple of **f0 contour**, **spectral envelope** and **aperiodicity**.
    """
    pass
