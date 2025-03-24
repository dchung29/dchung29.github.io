// src/context/LifeContext.js
import React, { createContext, useState } from 'react';

export const LifeContext = createContext();

export const LifeProvider = ({ children }) => {
  const [lives, setLives] = useState(3);

  const decrementLife = () => {
    setLives(prev => prev - 1);
  };

  const resetLives = () => {
    setLives(3);
  };

  return (
    <LifeContext.Provider value={{ lives, decrementLife, resetLives }}>
      {children}
    </LifeContext.Provider>
  );
};
