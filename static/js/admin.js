

 // NAV BUTTON LOGIC
  const navBtns = document.querySelectorAll('.nav-btn');
  const sections = document.querySelectorAll('main > section');

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.section;

      sections.forEach(sec => {
        if (sec.id === target) {
          sec.classList.add('visible-section');
          sec.classList.remove('hidden-section');
        } else {
          sec.classList.add('hidden-section');
          sec.classList.remove('visible-section');
        }
      });

      // Active button highlight
      navBtns.forEach(b => b.classList.remove('text-emerald-400'));
      btn.classList.add('text-emerald-400');
    });
  });

  // VIDEO CATEGORY FILTER
  const catButtons = document.querySelectorAll('.admin-cat-btn');
  const videoItems = document.querySelectorAll('.admin-video');

  catButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.dataset.category;
      videoItems.forEach(video => {
        video.style.display = (cat === 'all' || video.dataset.category === cat) ? 'flex' : 'none';
      });
    });
  });


  