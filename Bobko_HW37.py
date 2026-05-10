# task 1 - Воспроизведение мультимедиа
class AudioFileMixin:
    def play_audio(self) -> str:
        """
        Возвращает список аудиотреков.

        :return: Строка со списком аудиотреков
        """
        if not hasattr(self, "audio_tracks"):
            raise AttributeError(
                f"У объекта {self.__class__.__name__} отсутствует поле 'audio_tracks'"
            )

        tracks = "\n".join(self.audio_tracks)

        return (
            f"Воспроизведение аудио для {self.__class__.__name__}:\n"
            f"{tracks}"
        )


class VideoFileMixin:
    def play_video(self) -> str:
        """
        Возвращает список видеофайлов.

        :return: Строка со списком видеофайлов
        """
        if not hasattr(self, "video_files"):
            raise AttributeError(
                f"У объекта {self.__class__.__name__} отсутствует поле 'video_files'"
            )

        videos = "\n".join(self.video_files)

        return (
            f"Воспроизведение видео для {self.__class__.__name__}:\n"
            f"{videos}"
        )

# task 2 - Устройства
class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks: list[str]) -> None:
        """
        Инициализирует медиаплеер.

        :param audio_tracks: Список аудиотреков
        """
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks: list[str], video_files: list[str]) -> None:
        """
        Инициализирует ноутбук.

        :param audio_tracks: Список аудиотреков
        :param video_files: Список видеофайлов
        """
        self.audio_tracks = audio_tracks
        self.video_files = video_files


tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

player = MediaPlayer(tracks)

laptop = Laptop(tracks, movies)

print(player.play_audio())
print(laptop.play_audio())
print(laptop.play_video())
