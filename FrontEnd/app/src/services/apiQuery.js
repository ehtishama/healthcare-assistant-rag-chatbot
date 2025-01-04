const API_URL = 'http://127.0.0.1:8000/query_health_condition/';

export async function submitQuery(q) {
  try {
    const response = await fetch(`${API_URL}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: q }),
    });

    if (!response.ok) {
      throw new Error(`Server responded with status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error submitting query:", error);
    return { message: "An error occurred. Please try again later." };
  }
}
