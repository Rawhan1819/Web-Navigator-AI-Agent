// // src/App.jsx
// import React, { useState } from "react";

// export default function App() {
//   const [command, setCommand] = useState("");
//   const [output, setOutput] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState(null);

//   const handleExecute = async () => {
//     if (!command.trim()) return;
//     setLoading(true);
//     setError(null);
//     setOutput("");

//     try {
//       const res = await fetch("http://127.0.0.1:5000/generate", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ command }), // ✅ matches backend
//       });

//       if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
//       const data = await res.json();
//       setOutput(data.response || "No response from backend");
//     } catch (err) {
//       setError(err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="p-6 max-w-3xl mx-auto">
//       <h1 className="text-3xl font-bold mb-4 text-center">WebPilot AI Agent</h1>

//       <textarea
//         className="border p-3 w-full mb-4 h-28 resize-none rounded"
//         placeholder="Enter any command, e.g., 'search for laptops under 50k and list top 5'"
//         value={command}
//         onChange={(e) => setCommand(e.target.value)}
//       />

//       <button
//         className={`bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 ${
//           loading ? "opacity-50 cursor-not-allowed" : ""
//         }`}
//         onClick={handleExecute}
//         disabled={loading}
//       >
//         {loading ? "Executing..." : "Execute"}
//       </button>

//       {error && (
//         <div className="text-red-600 mt-4">
//           <strong>Error:</strong> {error}
//         </div>
//       )}

//       {output && (
//         <div className="bg-gray-100 p-4 rounded shadow mt-6 whitespace-pre-line">
//           <h2 className="font-semibold text-xl mb-2">Response:</h2>
//           <p>{output}</p>
//         </div>
//       )}
//     </div>
//   );
// }

// frontend/src/App.jsx

// -------------------------------------------------------------------------


// import React, { useState } from "react";

// function App() {
//   const [command, setCommand] = useState("");
//   const [results, setResults] = useState([]);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState(null);

//   const executeCommand = async () => {
//     setLoading(true);
//     setError(null);
//     setResults([]);

//     try {
//       const res = await fetch("http://127.0.0.1:5000/execute", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ command }),
//       });

//       if (!res.ok) throw new Error("HTTP error " + res.status);
//       const data = await res.json();

//       if (data.error) setError(data.error);
//       else setResults(data.results);
//     } catch (err) {
//       setError("Failed to fetch response from backend: " + err.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
//       <h1>WebPilot AI Agent</h1>

//       <textarea
//         rows="2"
//         cols="60"
//         value={command}
//         onChange={(e) => setCommand(e.target.value)}
//         placeholder="Type your command, e.g. search for best budget smartphones"
//         style={{ padding: "10px" }}
//       />
//       <br />
//       <button
//         onClick={executeCommand}
//         style={{
//           marginTop: "10px",
//           padding: "8px 16px",
//           background: "#007bff",
//           color: "#fff",
//           border: "none",
//           borderRadius: "4px",
//           cursor: "pointer",
//         }}
//       >
//         Execute
//       </button>

//       <h2>Response:</h2>
//       {loading && <p>Loading...</p>}
//       {error && <p style={{ color: "red" }}>{error}</p>}
//       <ul>
//         {results.map((item, idx) => (
//           <li key={idx} style={{ marginBottom: "20px" }}>
//             <a href={item.link} target="_blank" rel="noopener noreferrer">
//               <h3>{item.title}</h3>
//             </a>
//             {item.screenshot && (
//               <img
//                 src={`http://127.0.0.1:5000/screenshot/${item.screenshot.split("/").pop()}`}
//                 alt="screenshot"
//                 style={{ maxWidth: "500px", display: "block", margin: "10px 0" }}
//               />
//             )}
//             <p>{item.content}</p>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default App;

import React, { useState } from "react";
import "./App.css";

function App() {
  const [command, setCommand] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const executeCommand = async () => {
    setLoading(true);
    setError(null);
    setResults([]);

    try {
      const res = await fetch("http://127.0.0.1:5000/execute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command }),
      });

      const data = await res.json();
      if (data.error) setError(data.error);
      else setResults(data.results);
    } catch (err) {
      setError("Failed to fetch response: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <h1>WebPilot AI Agent</h1>
          <p>Search the web intelligently, view snippets and screenshots instantly.</p>
          <div className="hero-search">
            <textarea
              value={command}
              onChange={(e) => setCommand(e.target.value)}
              placeholder="Type your command, e.g., search for AI news 2025"
              rows="2"
            />
            <button onClick={executeCommand}>
              {loading ? "Searching..." : "Execute"}
            </button>
          </div>
          {error && <p className="error">{error}</p>}
        </div>
      </section>

      {/* Site Description */}
      <section className="description-section">
        <h2>About WebPilot AI Agent</h2>
        <p>
          WebPilot AI Agent fetches top search results along with full-page screenshots and content snippets. Perfect for research, shopping, news, and more.
        </p>
      </section>

      {/* Results */}
      <div className="results-container">
        {results.map((item, idx) => (
          <div key={idx} className="result-card">
            <div className="url-bar">{item.link}</div>
            {item.thumbnail && item.screenshot && (
              <a
                href={`http://127.0.0.1:5000/screenshot/${item.screenshot.split("/").pop()}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <img
                  src={`http://127.0.0.1:5000/thumbnail/${item.thumbnail.split("/").pop()}`}
                  alt="thumbnail"
                  className="screenshot"
                  loading="lazy"
                />
              </a>
            )}
            <div className="result-content">
              <a
                href={item.link}
                target="_blank"
                rel="noopener noreferrer"
                className="result-title"
              >
                {item.title}
              </a>
              <p className="snippet">{item.content}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Footer */}
      <footer className="app-footer">
        &copy; 2025 WebPilot AI Agent. All rights reserved.
      </footer>
    </div>
  );
}

export default App;




