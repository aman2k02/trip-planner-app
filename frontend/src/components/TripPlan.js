const getEventDetails = (type) => {
  switch (type) {
    case "drive":
      return { label: "DRIVE", icon: "🚚" };
    case "break":
      return { label: "BREAK", icon: "☕" };
    case "rest":
      return { label: "REST", icon: "🛌" };
    case "pickup":
      return { label: "PICKUP", icon: "📦" };
    case "dropoff":
      return { label: "DROPOFF", icon: "📍" };
    case "fuel":
      return { label: "FUEL STOP", icon: "⛽" };
    case "cycle_reset":
      return { label: "34hr RESET", icon: "🔄" };
    default:
      return { label: type.toUpperCase(), icon: "👉" };
  }
};

const TripPlan = ({ plan }) => {
  return (
    <div style={{ marginTop: "20px" }}>
      <h2 style={{ marginBottom: "15px" }}>📊 Trip Plan</h2>

      {/* 🔹 No plan */}
      {!plan || plan.length === 0 ? (
        <p>⚠️ No trip plan available</p>
      ) : (
        plan.map((day) => (
          <div
            key={day.day}
            style={{
              border: "1px solid #ddd",
              padding: "15px",
              marginBottom: "20px",
              borderRadius: "10px",
              background: "#ffffff",
              boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
            }}
          >
            <h3 style={{ marginBottom: "10px" }}>📅 Day {day.day}</h3>

            {/* 🔹 Summary */}
            <p>
              <strong>Total Drive:</strong> {day.total_drive_hours || 0} hrs
            </p>
            <p>
              <strong>Distance Covered:</strong> {day.total_distance || 0} km
            </p>

            <hr />

            {/* 🔹 Events */}
            {day.events.map((e, i) => {
              const { label, icon } = getEventDetails(e.type);

              return (
                <p key={i} style={{ margin: "6px 0" }}>
                  {icon} <strong>{label}</strong> — {e.hours} hrs
                </p>
              );
            })}
          </div>
        ))
      )}
    </div>
  );
};

export default TripPlan;