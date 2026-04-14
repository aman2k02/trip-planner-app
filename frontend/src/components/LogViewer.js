const LogViewer = ({ logs }) => {
  return (
    <div style={{ marginTop: "20px" }}>
      <h2>📋 ELD Logs</h2>

      {!logs || logs.length === 0 ? (
        <p>⚠️ No logs available</p>
      ) : (
        logs.map((log, i) => (
          <div key={i} style={{ marginBottom: "20px" }}>
            <p><strong>Day {i + 1}</strong></p>

            <img
              src={`http://127.0.0.1:8000${log}`}
              alt="log"
              style={{
                maxWidth: "400px",   // 🔥 FIXED SIZE
                width: "100%",
                borderRadius: "8px",
                boxShadow: "0 2px 6px rgba(0,0,0,0.2)"
              }}
              onError={(e) => {
                e.target.src = "";
                e.target.alt = "Failed to load log";
              }}
            />
          </div>
        ))
      )}
    </div>
  );
};

export default LogViewer;