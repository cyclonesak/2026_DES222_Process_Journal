# Prequel One
Setting up the Journal based on week 5 learning materials
# Prequel 2
Picture from my phone, a ship at sea, in a place it shouldn't be, sailing close to the rocks - means nothing ... 😄
![Ship at sea](/images/ship_at_sea.jpg)
<!-- <p align="center"><img src="/images/ship_at_sea.jpg" width="512" height="682"></p> -->
# Prequel 3
Added the [Youtube solution](https://christianheilmann.com/2022/09/14/quick-tip-embedding-youtube-videos-in-github-pages/) _includes folder.
The proof video is one of mine.
{% include youtube.html id="lRtFz77kVhU" %}
---
# Now the real deal...
---
---
# Entry 1 - Monday 17 August 2026
- Roughed out a concept and plan in the [README.md](/README.md) file

<div id="readme-window" style="
    border:1px solid #ccc;
    padding:20px;
    background:#fafafa;
    max-height:600px;
    overflow-y:auto;
"></div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
fetch("https://raw.githubusercontent.com/cyclonesak/2026_DES222_Process_Journal/main/README.md")
  .then(response => response.text())
  .then(text => {
    document.getElementById("readme-window").innerHTML = marked.parse(text);
  });
</script>



