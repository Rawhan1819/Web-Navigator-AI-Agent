const API_URL = import.meta.env.VITE_API_URL;

export async function executeCommand(command) {
  try {
    const response = await fetch(`${API_URL}/api/agents/execute`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error executing command:", error);
  }
}
