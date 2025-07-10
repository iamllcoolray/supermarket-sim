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
  } else {
    alert("Error submitting transaction.");
  }
}
