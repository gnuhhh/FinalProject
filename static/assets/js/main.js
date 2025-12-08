/**
* Template Name: Mentor
* Template URL: https://bootstrapmade.com/mentor-free-education-bootstrap-theme/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function () {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Chatbot Widget
   * Khởi tạo sau khi trang tải để đảm bảo phần tử đã tồn tại
   */
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  window.addEventListener('load', function () {
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotWindow = document.getElementById('chatbot-window');
    const chatbotClose = document.getElementById('chatbot-close');
    const chatbotForm = document.getElementById('chatbot-form');
    const chatbotInput = document.getElementById('chatbot-input');
    const chatbotMessages = document.getElementById('chatbot-messages');

    if (!chatbotToggle || !chatbotWindow) return; // Không có widget

    function appendMessage(text, role) {
      const div = document.createElement('div');
      div.className = `chatbot-message ${role}`;
      div.textContent = text;
      chatbotMessages.appendChild(div);
      chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    function setLoading(loading) {
      if (loading) {
        const div = document.createElement('div');
        div.className = 'chatbot-message bot';
        div.dataset.loading = '1';
        div.textContent = 'Đang soạn trả lời...';
        chatbotMessages.appendChild(div);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
      } else {
        const loadingNode = chatbotMessages.querySelector('[data-loading="1"]');
        if (loadingNode) loadingNode.remove();
      }
    }

    function toggleChatbot(open) {
      const willOpen = open !== undefined ? open : !chatbotWindow.classList.contains('open');
      chatbotWindow.classList.toggle('open', willOpen);
      chatbotWindow.setAttribute('aria-hidden', willOpen ? 'false' : 'true');
      if (willOpen) {
        setTimeout(() => {
          chatbotInput && chatbotInput.focus();
          // Scroll xuống cuối để hiển thị tin nhắn mới nhất
          chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
        }, 100);
      }
    }

    chatbotToggle.addEventListener('click', () => toggleChatbot(true));
    chatbotClose && chatbotClose.addEventListener('click', () => toggleChatbot(false));

    chatbotForm && chatbotForm.addEventListener('submit', async function (e) {
      e.preventDefault();
      const message = chatbotInput.value.trim();
      if (!message) return;
      appendMessage(message, 'user');
      chatbotInput.value = '';
      setLoading(true);
      try {
        const csrfToken = getCookie('csrftoken');
        const resp = await fetch(window.location.pathname, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken || '',
            'Accept': 'application/json'
          },
          body: new URLSearchParams({ message })
        });

        let data;
        try {
          data = await resp.json();
        } catch (parseErr) {
          throw new Error('Phản hồi không hợp lệ');
        }

        setLoading(false);
        console.log('Chatbot response status:', resp.status, 'data:', data);
        if (!resp.ok) {
          const errorMsg = data.error || `Lỗi ${resp.status}: Yêu cầu thất bại, vui lòng thử lại.`;
          appendMessage(errorMsg, 'bot');
          return;
        }
        appendMessage(data.response || 'Xin lỗi, hiện chưa có phản hồi.', 'bot');
      } catch (err) {
        setLoading(false);
        appendMessage('Có lỗi xảy ra, vui lòng thử lại sau.', 'bot');
      }
    });
  });

})();