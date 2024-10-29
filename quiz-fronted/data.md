# Quiz Game Application

This is a simple multi-level quiz game built using a Flask backend and a JavaScript/HTML frontend. Players answer questions and progress through multiple levels based on their performance.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Game Structure](#game-structure)
- [API Endpoints](#api-endpoints)

## Project Overview

This quiz game app allows users to start a quiz, answer questions across multiple levels, and select a specialized path after reaching Level 2 (BCA or B.Tech). Scores are tracked, and users progress through levels based on their performance.

## Features

- **Multi-level quiz**: Players answer questions on each level, and their progress is based on their score.
- **Path Selection**: After Level 2, players can choose between BCA and B.Tech paths for Level 3.
- **Score Tracking**: Scores are calculated based on correct answers, and the user’s progress is stored in memory.

## Technologies

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Cross-Origin Resource Sharing (CORS)**: Enabled with `flask-cors` to allow the frontend to communicate with the backend.

## Setup and Installation

### Prerequisites

- Python 3.x
- Node.js (optional, only if you want to use a different server to serve the frontend)
  
Open the frontend by going to http://127.0.0.1:8000 in a web browser.
