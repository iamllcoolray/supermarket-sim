let selectedItems = new Set();

function toggleItem(item) {
  const button = document.querySelector(`button[data-item="${item}"]`);
  if (selectedItems.has(item)) {
    selectedItems.delete(item);
    button.classList.remove("selected");
  } else {
    selectedItems.add(item);
    button.classList.add("selected");
  }
}

async function submitTransaction() {
  const response = await fetch("/submit", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ items: Array.from(selectedItems) })
  });

  if (response.ok) {
    alert("Transaction submitted!");
    selectedItems.clear();
    document.querySelectorAll(".item-button").forEach(btn => btn.classList.remove("selected"));

    updateTransactionCount();  // ✅ Add this line
  } else {
    alert("Error submitting transaction.");
  }
}

function clearMiningData() {
  fetch("/clear", { method: "POST" })
    .then(response => {
      if (!response.ok) throw new Error("Clear failed");
      return response.json();
    })
    .then(data => {
      console.log("🧹 Clear response:", data);
      alert("Transactions cleared!");

      updateTransactionCount();  // ✅ Add this line
    })
    .catch(err => {
      console.error("❌ Error clearing data:", err);
      alert("Failed to clear data. Check console.");
    });
}

function updateTransactionCount() {
  fetch("/count")
    .then(res => res.json())
    .then(data => {
      const countElement = document.getElementById("transaction-count");
      countElement.textContent = `🧾 Stored Transactions: ${data.count}`;
    });
}

document.addEventListener("DOMContentLoaded", updateTransactionCount);
