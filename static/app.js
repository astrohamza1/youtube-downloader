document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("download-form");
  const urlInput = document.getElementById("url-input");
  const loading = document.getElementById("loading");
  const error = document.getElementById("error");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const url = urlInput.value.trim();

    if (!isValidYouTubeURL(url)) {
      showError("⚠️ الرجاء إدخال رابط YouTube صالح.");
      return;
    }

    loading.style.display = "block";
    error.style.display = "none";

    try {
      const response = await fetch("/download", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `url=${encodeURIComponent(url)}`
      });

      if (!response.ok) throw new Error("فشل تحميل الفيديو.");

      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = downloadUrl;
      a.download = "video.mp4";
      a.click();
      window.URL.revokeObjectURL(downloadUrl);

    } catch (err) {
      showError("❌ حدث خطأ أثناء التحميل.");
    } finally {
      loading.style.display = "none";
    }
  });

  function isValidYouTubeURL(url) {
    const pattern = /^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/.+$/;
    return pattern.test(url);
  }

  function showError(message) {
    error.textContent = message;
    error.style.display = "block";
  }
});
