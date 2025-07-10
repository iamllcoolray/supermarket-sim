let selectedItems = new Set();
function toggleItem(item) {
  if (selectedItems.has(item)) selectedItems.delete(item);
  else selectedItems.add(item);
}
async function submitTransaction() {
  const response = await fetch("/submit", {
    method: "POST", headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ items: Array.from(selectedItems) })
  });
  if (response.ok) {
    alert("Transaction submitted!"); selectedItems.clear();
  } else {
    alert("Error submitting transaction.");
  }
}