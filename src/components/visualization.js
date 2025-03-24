import React from 'react';

const Visualization = ({ src, alt }) => {
  return (
    <div className="visualization-container">
      <video key={src} controls width="100%" style={{ borderRadius: '8px' }}>
        <source src={src} type="video/mp4" />
        {alt}
      </video>
    </div>
  );
};

export default Visualization;