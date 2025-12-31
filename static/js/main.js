
/* AOS ANIMATIONS */
AOS.init();
document.addEventListener('DOMContentLoaded', () => {

  const VIDEOS_PER_PAGE = 3;
  let currentCategory = 'all';
  let visibleCount = VIDEOS_PER_PAGE;

  const cards = Array.from(document.querySelectorAll('.video-card'));
  const showMoreBtn = document.getElementById('show-more-btn');

  function updateVideos(reset = false) {
    if (reset) visibleCount = VIDEOS_PER_PAGE;

    const filtered = cards.filter(card =>
      currentCategory === 'all' || card.dataset.category === currentCategory
    );

    // Hide all cards
    cards.forEach(card => {
      card.style.display = 'none';
    });

    // Show required cards
    filtered.slice(0, visibleCount).forEach(card => {
      card.style.display = 'block';
    });

    // Show / hide Show More button
    if (visibleCount < filtered.length) {
      showMoreBtn.classList.remove('hidden');
    } else {
      showMoreBtn.classList.add('hidden');
    }
  }

  // Category filter
  document.querySelectorAll('.category-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      currentCategory = btn.dataset.category;
      updateVideos(true);
    });
  });

  // Show more
  showMoreBtn.addEventListener('click', () => {
    visibleCount += VIDEOS_PER_PAGE;
    updateVideos();
  });

  updateVideos(true);
});

/* FEEDBACK MODAL */
const openBtn = document.getElementById('open-feedback');
const closeBtn = document.getElementById('close-feedback');
const modal = document.getElementById('feedback-modal');

openBtn.onclick = () => modal.classList.remove('hidden');
closeBtn.onclick = () => modal.classList.add('hidden');

/* FLATPICKR */
flatpickr("#datepicker", {
  dateFormat: "Y-m-d",
  minDate: "today",
  allowInput: true
});

/* STAR RATING */
const stars = document.querySelectorAll('.star-rating span');
const ratingInput = document.getElementById('rating-value');

stars.forEach((star, index) => {
  star.addEventListener('click', () => {
    const rating = index + 1;
    ratingInput.value = rating;
    stars.forEach((s, i) => s.classList.toggle('active', i < rating));
  });
});

/* FEEDBACK FORM */
const feedbackForm = document.getElementById('feedback-form');
const successPopup = document.getElementById('feedback-success');
const closeSuccess = document.getElementById('close-success');
const feedbackModal = document.getElementById('feedback-modal');

feedbackForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  await fetch(feedbackForm.action, { method: 'POST', body: new FormData(feedbackForm) });
  feedbackModal.classList.add('hidden');
  successPopup.classList.remove('hidden');
  feedbackForm.reset();
});

closeSuccess.addEventListener('click', () => {
  successPopup.classList.add('hidden');
});

document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll(".section-animate");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("active");
        } else {
          entry.target.classList.remove("active"); 
          // 👆 this allows animation again when scrolling back
        }
      });
    },
    {
      threshold: 0.2,
      rootMargin: "0px 0px -80px 0px"
    }
  );

  sections.forEach(section => observer.observe(section));
});
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".video-card");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("show");
          observer.unobserve(entry.target); // animate once
        }
      });
    },
    {
      threshold: 0.15,       // appears early (mobile friendly)
      rootMargin: "0px 0px -50px 0px"
    }
  );

  cards.forEach(card => observer.observe(card));
});
