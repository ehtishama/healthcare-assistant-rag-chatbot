const API_URL = import.meta.env.VITE_API_BASE_URL;

export async function submitQuery(q, thread_id) {
  try {
    const response = await fetch(`${API_URL}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: q, thread_id }),
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
