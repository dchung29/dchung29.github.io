import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Board from './components/Board';
import Question from './components/questions';
import questionsData from './data/questions';
import './App.css';

function generateBoardData() {
  const headers = [100, 200, 300];
  const totalSquares = 15; // 3 columns (for each topic) * 5 rows (for 5 questions per topic)
  let boardQuestions = [];

  // Fill boardQuestions: use questionsData for available questions; otherwise use dummy questions
  for (let i = 0; i < totalSquares; i++) {
    if (i < questionsData.length) {
      let q = questionsData[i];


      if (q.value === undefined) {
        q = { ...q, value: headers[Math.floor(i / 5)] };
      }
      boardQuestions.push(q);
    } else {
      const header = headers[Math.floor(i / 5)];
      boardQuestions.push({
        prompt: `Dummy question ${header}-${(i % 5) + 1}`,
        value: header,
        options: [
          { text: 'Correct', isCorrect: true },
          { text: 'Wrong', isCorrect: false }
        ]
      });
    }
  }

  // group questions into 3 columns (each with 5 questions)
  return headers.map((header, colIndex) => {
    return {
      header: header,
      questions: boardQuestions.slice(colIndex * 5, colIndex * 5 + 5)
    };
  });
}

function App() {
  const [boardData, setBoardData] = useState([]);
  const [answeredQuestions, setAnsweredQuestions] = useState([]);
  const [teamScores, setTeamScores] = useState({ team1: 0, team2: 0 });
  const [currentTeam, setCurrentTeam] = useState(1);
  const [gameCompleted, setGameCompleted] = useState(false);
  const [winner, setWinner] = useState("");

  useEffect(() => {
    const data = generateBoardData();
    setBoardData(data);
    setAnsweredQuestions(data.map(col => Array(col.questions.length).fill(false)));
  }, []);

  useEffect(() => {
    if (answeredQuestions.length > 0) {
      const finished = answeredQuestions.every(col => col.every(val => val === true));
      if (finished) {
        setGameCompleted(true);
        let winnerText = "";
        if (teamScores.team1 > teamScores.team2) {
          winnerText = "Team 1 wins!";
        } else if (teamScores.team2 > teamScores.team1) {
          winnerText = "Team 2 wins!";
        } else {
          winnerText = "It's a tie!";
        }
        setWinner(winnerText);
      }
    }
  }, [answeredQuestions, teamScores]);

  const handleQuestionAnswered = (colIndex, rowIndex, questionValue, isCorrect) => {
    if (isCorrect) {
      setAnsweredQuestions(prev => {
        const newAnswered = prev.map(arr => arr.slice());
        newAnswered[colIndex][rowIndex] = true;
        return newAnswered;
      });
      setTeamScores(prev => {
        return currentTeam === 1
          ? { ...prev, team1: prev.team1 + questionValue }
          : { ...prev, team2: prev.team2 + questionValue };
      });
    }
    
    // Always alternate turn, regardless of correctness
    setCurrentTeam(prev => (prev === 1 ? 2 : 1));
  };

  const handleReplay = () => {
    setAnsweredQuestions(boardData.map(col => Array(col.questions.length).fill(false)));
    setTeamScores({ team1: 0, team2: 0 });
    setCurrentTeam(1);
    setGameCompleted(false);
  };

  return (
    <div className="app-container">
      <Router>
        <Routes>
          <Route
            path="/"
            element={<Board boardData={boardData} answeredQuestions={answeredQuestions} teamScores={teamScores} currentTeam={currentTeam} />}
          />
          {boardData.map((column, colIndex) =>
            column.questions.map((question, rowIndex) => (
              <Route
                key={`q-${colIndex}-${rowIndex}`}
                path={`/question/${colIndex}/${rowIndex}`}
                element={
                  <Question
                    question={question}
                    colIndex={colIndex}
                    rowIndex={rowIndex}
                    onAnswered={handleQuestionAnswered}
                  />
                }
              />
            ))
          )}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </Router>
      {gameCompleted && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h2>{winner}</h2>
            <button onClick={handleReplay}>Replay</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
