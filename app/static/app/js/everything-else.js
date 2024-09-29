    function getRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
    const cards = document.querySelectorAll('.everything-else-card');
    cards.forEach(card => {
      card.style.backgroundColor = getRandomColor();
    });



let currentlyPlaying;

function playSong(songUrl) {
    const audioPlayer = document.getElementById('audio-player');
    const audioSource = document.getElementById('audio-source');

    if (currentlyPlaying) {
        currentlyPlaying.pause(); // Остановить текущую песню
    }

    audioSource.src = songUrl; // Установить источник аудио
    audioPlayer.load();         // Загрузить новый источник
    audioPlayer.play();         // Воспроизвести аудио

    currentlyPlaying = audioPlayer; // Сохранить ссылку на текущий плеер
}

function pauseAudio() {
    const audioPlayer = document.getElementById('audio-player');
    audioPlayer.pause(); // Остановить воспроизведение
}