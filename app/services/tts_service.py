import os
import uuid

import azure.cognitiveservices.speech as speechsdk

from app.config import (
    AZURE_SPEECH_KEY,
    AZURE_SPEECH_REGION,
)


class TTSService:

    VOICE_MAP = {
        "en": "en-IN-NeerjaNeural",
        "hi": "hi-IN-SwaraNeural",
        "mr": "mr-IN-AarohiNeural",
        "ta": "ta-IN-PallaviNeural",
        "te": "te-IN-ShrutiNeural",
        "kn": "kn-IN-SapnaNeural",
        "ml": "ml-IN-SobhanaNeural",
        "gu": "gu-IN-DhwaniNeural",
        "bn": "bn-IN-TanishaaNeural",
        "pa": "pa-IN-GurleenNeural",
        "od": "or-IN-SubhasiniNeural",
    }

    @staticmethod
    def generate_speech(text: str, language: str):

        output_dir = "app/audio"
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{uuid.uuid4()}.mp3"
        output_path = os.path.join(output_dir, filename)

        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_SPEECH_KEY,
            region=AZURE_SPEECH_REGION,
        )

        voice = TTSService.VOICE_MAP.get(
            language,
            "en-IN-NeerjaNeural",
        )

        speech_config.speech_synthesis_voice_name = voice

        audio_config = speechsdk.audio.AudioOutputConfig(
            filename=output_path
        )

        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config,
            audio_config=audio_config,
        )

        result = synthesizer.speak_text_async(text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return filename

        raise Exception("Speech synthesis failed.")