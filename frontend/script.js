const chatBox = document.getElementById("chatBox");
const input = document.getElementById("messageInput");

// Scam Intelligence fields
const upiEl = document.getElementById("upi");
const bankEl = document.getElementById("bank");
const linkEl = document.getElementById("links");

// ---------- Helpers ----------
function scrollBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}

function addMessage(text, type) {
  const hint = document.querySelector(".hint");
  if (hint) hint.remove();

  const div = document.createElement("div");
  div.className = `msg ${type}`;
  div.innerText = text;
  chatBox.appendChild(div);
  scrollBottom();
}

// ---------- AI Logic ----------
function generateAIReply(message) {
  const msg = message.toLowerCase();

  // greetings
  if (msg === "hi" || msg === "hello" || msg === "hlw" || msg === "hey") {
    return "Hello, aap kaun si service ke liye contact kar rahe ho?";
  }

  if (msg.includes("blocked") || msg.includes("suspended")) {
    return "Mera account kaunsa service me block hua hai? Exact reason batao.";
  }

  if (msg.includes("upi") || msg.includes("send money") || msg.includes("payment")) {
    return "Payment se pehle reason clear karo, bank ne officially kya bola hai?";
  }

  if (msg.includes("link") || msg.includes("http")) {
    return "Ye official website nahi lag rahi, bank ka proper domain bhejo.";
  }

  if (msg.includes("urgent") || msg.includes("immediately") || msg.includes("warning")) {
    return "Main verify kar raha hoon, bina confirmation ke payment possible nahi hai.";
  }

  if (msg.includes("legal") || msg.includes("case") || msg.includes("notice")) {
    return "Legal notice ka reference number aur email proof bhejo.";
  }

  return "Thoda aur detail me samjhao, mujhe abhi clear nahi ho raha.";
}

// ---------- Intelligence Extraction ----------
function extractIntelligence(text) {
  // UPI
  const upiMatch = text.match(/[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}/);
  if (upiMatch) {
    upiEl.innerText = upiMatch[0];
  }

  // Links
  const linkMatch = text.match(/https?:\/\/[^\s]+/);
  if (linkMatch) {
    linkEl.innerText = linkMatch[0];
  }
}

// ---------- Send Message ----------
function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  addMessage("Scammer: " + text, "scammer");
  extractIntelligence(text);
  input.value = "";

  // AI delay (human-like)
  setTimeout(() => {
    const reply = generateAIReply(text);
    addMessage("Honeypot: " + reply, "agent");
  }, 2000);
}

// ---------- Enter Key Support ----------
input.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});
