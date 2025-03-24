import React, { useContext } from 'react';
import { LifeContext } from '../context/life';
import './life_indicator.css';

const LifeIndicator = () => {
  const { lives } = useContext(LifeContext);
  return (
    <div className="life-indicator">
      Lives: {lives}
    </div>
  );
};

export default LifeIndicator;
