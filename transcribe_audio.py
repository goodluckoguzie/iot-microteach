import whisper
import sys

def transcribe_audio(audio_path):
    """Transcribe audio file using Whisper"""
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    
    print(f"Transcribing {audio_path}...")
    result = model.transcribe(audio_path)
    
    print("\n" + "="*80)
    print("TRANSCRIPTION:")
    print("="*80)
    print(result["text"])
    print("="*80)
    
    # Save to file
    output_file = "transcription.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"\nTranscription saved to {output_file}")
    return result["text"]

if __name__ == "__main__":
    audio_file = "Questions.m4a"
    transcribe_audio(audio_file)

