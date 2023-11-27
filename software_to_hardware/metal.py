import pyaudio
import time
from math import log10
import audioop

class SoundMonitor:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.WIDTH = 2
        self.RATE = int(self.p.get_default_input_device_info()['defaultSampleRate'])
        self.DEVICE = self.p.get_default_input_device_info()['index']
        self.rms_values = []

    def callback(self, in_data, frame_count, time_info, status):
        rms = audioop.rms(in_data, self.WIDTH) / 32767
        self.rms_values.append(rms)
        return in_data, pyaudio.paContinue

    def record_for_seconds(self, duration=5):
        stream = self.p.open(
            format=self.p.get_format_from_width(self.WIDTH),
            input_device_index=self.DEVICE,
            channels=1,
            rate=self.RATE,
            input=True,
            output=False,
            stream_callback=self.callback
        )
        stream.start_stream()

        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            pass  # Allow the user to interrupt the program with Ctrl+C

        stream.stop_stream()
        stream.close()

        return self.calculate_average_rms()

    def calculate_average_rms(self):
        if not self.rms_values:
            return 0  # Return 0 if no values recorded
        return sum(self.rms_values) / len(self.rms_values)

    def close(self):
        self.p.terminate()

def run_mic():
    monitor = SoundMonitor()
    average_db = monitor.record_for_seconds()
    output = 20 * log10(average_db)
    print(output)
    monitor.close()
    return output > -5

