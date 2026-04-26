var mobileMenuToggle = document.querySelector(".mobile-menu-toggle");
var navLinks = document.querySelector(".nav-links");
var navbar = document.querySelector(".nav-container");
var themeStyles = getComputedStyle(document.documentElement);
var navBackground = themeStyles.getPropertyValue("--nav-bg").trim();
var navBackgroundStrong = themeStyles.getPropertyValue("--nav-bg-strong").trim();
if (mobileMenuToggle && navLinks) {
    mobileMenuToggle.addEventListener("click", function () {
        mobileMenuToggle.classList.toggle("active");
        navLinks.classList.toggle("active");
    });
}
var navLinkItems = document.querySelectorAll(".nav-links a");
navLinkItems.forEach(function (link) {
    link.addEventListener("click", function () {
        mobileMenuToggle === null || mobileMenuToggle === void 0 ? void 0 : mobileMenuToggle.classList.remove("active");
        navLinks === null || navLinks === void 0 ? void 0 : navLinks.classList.remove("active");
    });
});
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (event) {
        event.preventDefault();
        var href = anchor.getAttribute("href");
        if (!href) {
            return;
        }
        var target = document.querySelector(href);
        if (target) {
            var offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: "smooth",
            });
        }
    });
});
var sections = document.querySelectorAll("section[id]");
var navItems = document.querySelectorAll(".nav-links a");
function highlightNavigation() {
    var scrollPosition = window.scrollY + 150;
    sections.forEach(function (section) {
        var sectionTop = section.offsetTop;
        var sectionHeight = section.offsetHeight;
        var sectionId = section.getAttribute("id");
        if (!sectionId) {
            return;
        }
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navItems.forEach(function (item) {
                item.classList.remove("active");
                if (item.getAttribute("href") === "#".concat(sectionId)) {
                    item.classList.add("active");
                }
            });
        }
    });
}
window.addEventListener("scroll", highlightNavigation);
window.addEventListener("load", highlightNavigation);
var observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
};
var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
        if (entry.isIntersecting) {
            var target = entry.target;
            target.style.opacity = "1";
            target.style.transform = "translateY(0)";
        }
    });
}, observerOptions);
var animatedElements = document.querySelectorAll(".timeline-item, .project-card, .education-card, .skill-category");
animatedElements.forEach(function (element) {
    element.style.opacity = "0";
    element.style.transform = "translateY(30px)";
    element.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(element);
});
window.addEventListener("scroll", function () {
    var currentScroll = window.pageYOffset;
    if (!navbar) {
        return;
    }
    if (currentScroll > 100) {
        navbar.style.background = navBackgroundStrong;
        navbar.style.boxShadow = "0 2px 15px rgba(0, 0, 0, 0.15)";
    }
    else {
        navbar.style.background = navBackground;
        navbar.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.1)";
    }
});
window.addEventListener("load", function () {
    var heroElements = document.querySelectorAll(".hero-title, .hero-subtitle, .hero-description, .hero-buttons, .hero-social");
    heroElements.forEach(function (element, index) {
        setTimeout(function () {
            element.style.opacity = "1";
            element.style.transform = "translateY(0)";
        }, index * 150);
    });
});
var emailLinks = document.querySelectorAll('a[href^="mailto"]');
emailLinks.forEach(function (link) {
    link.addEventListener("contextmenu", function (event) {
        event.preventDefault();
        var href = link.getAttribute("href");
        if (!href) {
            return;
        }
        var email = href.replace("mailto:", "");
        navigator.clipboard.writeText(email).then(function () {
            var tooltip = document.createElement("span");
            tooltip.textContent = "Email copied!";
            tooltip.style.cssText = "\n                position: absolute;\n                background: var(--maroon);\n                color: white;\n                padding: 0.5rem 1rem;\n                border-radius: 4px;\n                font-size: 0.875rem;\n                pointer-events: none;\n                z-index: 1000;\n                animation: fadeInUp 0.3s ease;\n            ";
            document.body.appendChild(tooltip);
            var rect = link.getBoundingClientRect();
            tooltip.style.left = "".concat(rect.left + rect.width / 2 - tooltip.offsetWidth / 2, "px");
            tooltip.style.top = "".concat(rect.top - tooltip.offsetHeight - 10, "px");
            setTimeout(function () {
                tooltip.remove();
            }, 2000);
        });
    });
});
if ("IntersectionObserver" in window) {
    var imageObserver_1 = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                var image = entry.target;
                var source = image.dataset.src;
                if (source) {
                    image.src = source;
                    image.removeAttribute("data-src");
                    imageObserver_1.unobserve(image);
                }
            }
        });
    });
    document.querySelectorAll("img[data-src]").forEach(function (image) {
        imageObserver_1.observe(image);
    });
}
function debounce(func, wait) {
    if (wait === void 0) { wait = 10; }
    var timeout;
    return function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        var later = function () {
            window.clearTimeout(timeout);
            func.apply(void 0, args);
        };
        window.clearTimeout(timeout);
        timeout = window.setTimeout(later, wait);
    };
}
window.addEventListener("scroll", debounce(highlightNavigation, 10));
