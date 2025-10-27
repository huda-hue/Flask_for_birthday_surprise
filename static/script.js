function showMessage() {
  const msg = document.getElementById("message");
  const music = document.getElementById('bg-music');

	// toggle pesan
	msg.classList.toggle('hidden');

	// mainkan musik
	music.play();
}
