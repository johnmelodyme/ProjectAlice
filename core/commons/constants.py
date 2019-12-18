VERSION = '1.0.0-a5'
DEFAULT_SITE_ID = 'default'
DEFAULT = 'default'
UNKNOWN_WORD = 'unknownword'
UNKNOWN_USER = 'unknownUser'
UNKNOWN_MANAGER = 'unknownManager'
UNKNOWN = 'unknown'
EVERYWHERE = 'everywhere'
ALL = 'all'
DUMMY = 'dummy'
DATABASE_FILE = 'system/database/data.db'

TOPIC_AUDIO_FRAME = 'hermes/audioServer/{}/audioFrame'
TOPIC_HOTWORD_DETECTED = 'hermes/hotword/default/detected'
TOPIC_WAKEWORD_DETECTED = 'hermes/hotword/{}/detected'
TOPIC_ASR_START_LISTENING = 'hermes/asr/startListening'
TOPIC_SESSION_STARTED = 'hermes/dialogueManager/sessionStarted'
TOPIC_SESSION_QUEUED = 'hermes/dialogueManager/sessionQueued'
TOPIC_SESSION_ENDED = 'hermes/dialogueManager/sessionEnded'
TOPIC_TEXT_CAPTURED = 'hermes/asr/textCaptured'
TOPIC_INTENT_NOT_RECOGNIZED = 'hermes/dialogueManager/intentNotRecognized'
TOPIC_INTENT_PARSED = 'hermes/nlu/intentParsed'
TOPIC_TTS_SAY = 'hermes/tts/say'
TOPIC_TTS_FINISHED = 'hermes/tts/sayFinished'
TOPIC_HOTWORD_TOGGLE_ON = 'hermes/hotword/toggleOn'
TOPIC_PLAY_BYTES = 'hermes/audioServer/{}/playBytes/{}'
TOPIC_START_SESSION = 'hermes/dialogueManager/startSession'
TOPIC_CONTINUE_SESSION = 'hermes/dialogueManager/continueSession'
TOPIC_END_SESSION = 'hermes/dialogueManager/endSession'
TOPIC_DIALOGUE_MANAGER_CONFIGURE = 'hermes/dialogueManager/configure'
TOPIC_TOGGLE_FEEDBACK_ON = 'hermes/feedback/sound/toggleOn'
TOPIC_TOGGLE_FEEDBACK_OFF = 'hermes/feedback/sound/toggleOff'
TOPIC_TOGGLE_FEEDBACK = 'hermes/feedback/sound/toggle{}'
TOPIC_STOP_LISTENING = 'hermes/asr/stopListening'
TOPIC_NLU_QUERY = 'hermes/nlu/query'
TOPIC_VAD_UP = 'hermes/voiceActivity/{}/vadUp'
TOPIC_VAD_DOWN = 'hermes/voiceActivity/{}/vadDown'
