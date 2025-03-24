import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import Visualization from './visualization';
import './questions.css';

const Question = ({ question, colIndex, rowIndex, onAnswered }) => {

  // Retrieve teamScores and currentTeam from location state
  const location = useLocation();
  const { teamScores, currentTeam } = location.state || {};
  const [feedback, setFeedback] = useState("");
  const [answeredCorrectly, setAnsweredCorrectly] = useState(false);
  const [attempted, setAttempted] = useState(false);
  const navigate = useNavigate();

  const categoryNames = ['Linear Transformations', 'Eigen', 'Null Space'];

  useEffect(() => {
    setFeedback("");
    setAnsweredCorrectly(false);
    setAttempted(false);
  }, [question, colIndex, rowIndex]);

  const handleOptionClick = (option) => {
    setAttempted(true);
    if (option.isCorrect) {
      setFeedback("Correct!");
      setAnsweredCorrectly(true);
      if (onAnswered) onAnswered(colIndex, rowIndex, question.value, true);
    } else {
      setFeedback("Incorrect.");
      if (onAnswered) onAnswered(colIndex, rowIndex, question.value, false);
    }
  };

  const handleNext = () => {
    navigate("/");
  };

  return (
    <div className="question-page">
      {/* Left column: The main "card" containing the question */}
      <div className="question-card">
        <div className="question-title">{categoryNames[colIndex]}</div>
        <div className="question-details">Question {rowIndex + 1} of 5</div>
        <div className="question-prompt">{question.prompt}</div>

        {question.visualization && (
          <div className="visualization-container">
            <Visualization src={question.visualization} alt="Visualization" />
          </div>
        )}

        <div className="options-container">
          {question.options.map((option, idx) => (
            <button
              key={idx}
              className="option-button"
              onClick={() => handleOptionClick(option)}
              disabled={answeredCorrectly}
            >
              {option.text}
            </button>
          ))}
        </div>

        <div className="feedback">{feedback}</div>

        {attempted && (
          <button className="option-button next-button" onClick={handleNext}>
            Back to Board
          </button>
        )}
      </div>

      {/* Right column: Score and additional info */}
      <div className="score-container">
        <div className="score-title">
          Team 1: {teamScores.team1}
        </div>
        <div className='score-title'>
          Team 2: {teamScores.team2}
        </div>
        <div className='score-title'>
          Current Turn: Team {currentTeam}
        </div>
      </div>
    </div>
  );
};

export default Question;
