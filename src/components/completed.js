import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { LifeContext } from '../context/life';
import './completed.css';

const Completed = () => {
  const { resetLives } = useContext(LifeContext);
  const navigate = useNavigate();

  const handleRestart = () => {
    resetLives();
    navigate("/");
  };

  return (
    <div className="completed-container">
      <h1>Congratulations!</h1>
      <p>You have successfully completed the quiz. We hope through visualizations, you were able to learn more about Linear Algebra!</p>
      <button className="restart-button" onClick={handleRestart}>
        Restart Quiz
      </button>
    </div>
  );
};

export default Completed;
