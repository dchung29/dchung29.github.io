import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Board.css';

const Board = ({ boardData, answeredQuestions, teamScores, currentTeam }) => {
  const navigate = useNavigate();
  
  const headerMap = {
    100: 'Linear Transformations',
    200: 'Eigen',
    300: 'Null Space'
  };

  const handleCardClick = (colIndex, rowIndex) => {
    if (!answeredQuestions[colIndex][rowIndex]) {
      navigate(`/question/${colIndex}/${rowIndex}`, { 
        state: { teamScores, currentTeam } 
      });
    }
  };

  return (
    <div className="board-wrapper">
      <div className="board-title">312 Jeopardy!</div>
      <div className="board-container">
        <div className="board-info">
          Team 1: {teamScores.team1} | Team 2: {teamScores.team2} | Current Turn: Team {currentTeam}
        </div>
        {boardData.map((column, colIndex) => (
          <div key={`col-${colIndex}`} className="board-column">
            <div className="board-header">{headerMap[column.header] || column.header}</div>
            {column.questions.map((question, rowIndex) => {
              const answered = answeredQuestions[colIndex][rowIndex];
              return (
                <div
                  key={`q-${colIndex}-${rowIndex}`}
                  className={`board-card ${answered ? 'answered' : ''}`}
                  onClick={() => handleCardClick(colIndex, rowIndex)}
                >
                  {answered ? 'Completed' : question.value}
                </div>
              );
            })}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Board;
