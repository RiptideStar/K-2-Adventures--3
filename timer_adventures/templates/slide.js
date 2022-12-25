import React, { useState } from 'react';

function Slideshow() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const slides = [
    'Slide 1',
    'Slide 2',
    'Slide 3',
    'Slide 4',
  ];

  function handleClick() {
    setCurrentSlide((currentSlide + 1) % slides.length);
  }

  return (
    <div onClick={handleClick}>
      {slides[currentSlide]}
    </div>
  );
}