// src/components/GameOver.js
import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { LifeContext } from '../context/life';
import './gameover.css';

const GameOver = () => {
  const { resetLives } = useContext(LifeContext);
  const navigate = useNavigate();

  const handleRestart = () => {
    resetLives();
    navigate("/");
  };

  return (
    <div className="gameover-container">
      <h1>Game Over</h1>
      <button onClick={handleRestart}>Try Again</button>
    </div>
  );
};

export default GameOver;
