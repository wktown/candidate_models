import logging

from brainio.fetch import get_stimulus_set
from candidate_models.model_commitments import brain_translated_pool

_logger = logging.getLogger(__name__)

def get_activations(model, layers, stimulus_set):
    stimuli = get_stimulus_set(stimulus_set)
    return model(stimuli, layers=layers)
