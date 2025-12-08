# 🔥 BRUTAL PRESENTATION CRITIQUE
## Current IoT Micro-Teach vs. Supervisor Requirements

**Date:** December 2024  
**Presentation URL:** http://localhost:8000  
**Grade:** **D- (Critical Failure)**

---

## 🚨 CRITICAL ERRORS (Interview Killers)

### **1. WRONG TITLE - IMMEDIATE DISQUALIFICATION**
**Current Title (Line 6):**
```html
<title>PhD Viva Presentation - Goodluck Oguzie</title>
```

**Impact:** ❌ **This is NOT a PhD viva! You're in a JOB INTERVIEW!**
- Shows you copied from another presentation without checking
- Demonstrates lack of attention to detail
- First impression = unprepared candidate

**Should Be:**
```html
<title>Introduction to IoT: Smart Home Security System - Interview Micro-Teach</title>
```

---

### **2. BROKEN LINKS - PRESENTATION WON'T LOAD**
**Current Code (Lines 10-19):**
```html
<link rel="stylesheet" href="dist/reset.css" />
<link rel="stylesheet" href="dist/reveal.css" />
<link rel="stylesheet" href="dist/theme/white.css" />

<script src="dist/reveal.js"></script>
<script src="plugin/notes/notes.js"></script>
```

**Impact:** ❌ **THESE FILES DON'T EXIST IN YOUR PRESENTATION FOLDER!**
- Your presentation won't load during the interview
- You'll waste 5 minutes troubleshooting in front of the panel
- **Instant failure**

**What You SHOULD Have (Working CDN Links):**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/white.css">
<script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
```

---

### **3. MISSING CRITICAL CONTENT - SUPERVISOR'S #1 REQUIREMENT**

**Supervisor Said (Transcription):**
> "So, **after you've demonstrated on TinkerCard, you can mention that for the sake of hands-on**, because you show from your experience, you've seen that students get more excited when you show them the real physical device... **after the TinkerCard, if you show us through the camera, and say, everything I've just done on TinkerCard, here are the same devices I have physically at home.**"

**Current Presentation:** ❌ **NO mention of physical devices after Tinkercad**
**Current Slide 6:** Mentions physical hardware but **doesn't show you holding actual Arduino/PIR sensor via camera**

**Impact:** **Fails to demonstrate "hands-on pedagogy" - the supervisor's most emphasized point**

---

## 📊 SLIDE-BY-SLIDE BRUTAL ASSESSMENT

### **Slide 1: Title Slide**
**Grade: F (Failure)**

**Current Design:**
- Dark background (#01404f)
- Image in top-right corner (tiny, meaningless)
- Left-aligned text
- "Dr. Goodluck Oguzie" - Are you a doctor? If not, remove "Dr."
- Email: goguzie@qa.com (Is this real? Looks fake)

**Problems:**
1. ❌ **Unprofessional email** - Looks like a placeholder
2. ❌ **Date says "December 2025"** - That's in the FUTURE! Interview is NOW (Dec 2024)
3. ❌ **Poor space utilization** - Everything crammed to left, right side wasted
4. ❌ **Dark background (#01404f)** - Hard to read, depressing, not engaging

**Comparison to Your PhD Viva (https://goodluckoguzie.github.io/Viva/):**
- PhD viva: Clean, centered, professional hierarchy
- Current: Messy, left-aligned, poor visual balance

**Supervisor's Requirement:**
> "the worst thing to do is **don't have more than five, six slides**"

✅ You have 6 slides (GOOD)  
❌ But Slide 1 looks unprofessional (BAD)

---

### **Slide 2: Learning Objectives**
**Grade: C**

**Current Design:**
- Dark background
- Emoji 🎯 (unprofessional for university teaching)
- Three objectives (correct content)

**Problems:**
1. ❌ **Emojis** - You're teaching Level 4-6 HE students, not children
2. ❌ **"fade-left" animations** - Distracting, wastes time
3. ⚠️ **Dark background makes text hard to read**

**What Works:**
- ✅ Uses Bloom's taxonomy verbs (Define, Identify, Construct)
- ✅ Three clear, measurable objectives

**Supervisor's Expectation:**
> "The slide should just be to show us the **shock job, what you plan to do**, and then immediately **jump to the practicals**"

**Your slide:** Meets requirement but design is weak

---

### **Slide 3: What is IoT?**
**Grade: D+**

**Current Content:**
- Definition (correct)
- Key components (Sensors, Connectivity, Processing)
- Emojis: 👁️ 📡 🧠

**Critical Problems:**
1. ❌ **NO REAL-WORLD IMAGES** - Supervisor emphasized visual learning
2. ❌ **Just emojis and text** - Boring, not engaging
3. ❌ **No engagement questions** - Supervisor said "**engage with the audience**"

**Supervisor's Requirement (Transcription):**
> "**you should think aloud, engage with the audience**... before you do that, you show us. Get us to engage. And say something like, **if I wanted to build a smart home, for example. What would I think of? Use those type of prompting questions**"

**Your Slide 3:** ❌ **NO engagement questions visible**

**What's Missing:**
- Real IoT device images (Nest thermostat, Fitbit, smart car)
- Engagement question: "What IoT devices do you use daily?"
- Visual examples beyond emojis

---

### **Slide 4: The Challenge: Home Security**
**Grade: C-**

**Current Content:**
- Problem statement
- Solution (Motion-Activated Alarm)
- Flow diagram (INPUT → PROCESS → OUTPUT)

**Problems:**
1. ❌ **No visual diagram** - Just emojis and text
2. ❌ **No engagement question** - Missing opportunity
3. ❌ **"🚀 The Problem"** - Wrong emoji (🚀 = rocket/launch, not problem)

**Should Be:**
- ❌ should be 🔴 or ⚠️
- Add question: "What sensor detects body heat?" (from your script)
- Add visual: Simple home diagram showing where sensor would be placed

**Supervisor's Emphasis:**
> "**Get us to engage**... Use those type of **prompting questions** that are easy to answer, but to get us to **participate**"

---

### **Slide 5: Circuit Blueprint**
**Grade: F (Critical Failure)**

**Current Content:**
```html
<div style="...">
  <p style="color: white;">(Paste Tinkercad Screenshot Here)</p>
</div>
```

**Impact:** ❌ **YOU HAVE A PLACEHOLDER!** 

This is **WORSE than having no slide at all** because it shows:
- You didn't finish the presentation
- You're unprepared
- You don't take the interview seriously

**Supervisor's EXPLICIT Requirement:**
Your `Slides_Content.md` (Line 51) says:
> "**Paste a screenshot of your Tinkercad circuit here BEFORE you start the live demo**"

**Current State:** ❌ **PLACEHOLDER TEXT - NOT A SCREENSHOT**

**Impact on Interview:**
- Panel sees placeholder
- Assumes you're unprepared
- **Automatic failure**

**What You MUST Do:**
1. Open Tinkercad
2. Build the circuit (Arduino + PIR + LED)
3. Take screenshot
4. Save as `circuit-diagram.png`
5. Replace placeholder

---

### **Slide 6: Summary & Next Steps**
**Grade: D**

**Current Content:**
- Recap (good)
- Next session mentions physical hardware
- "Any Questions?" prompt

**Critical Problems:**
1. ❌ **NO MENTION OF "HANDS-ON PEDAGOGY"** - Supervisor's key phrase
2. ❌ **NO CAMERA DEMONSTRATION** - Not mentioned in slides or speaker notes
3. ❌ **Missing the "Physical Transition" moment**

**Supervisor's EXACT Words (Transcription):**
> "**after the TinkerCard, if you show us through the camera, and say**, everything I've just done on TinkerCard, **here are the same devices I have physically at home**. But because this is an online interview, I'm not able to show you. However, **here is what I would have done if this was physical. Here is the sensor. Here is the cable. Here is the Raspberry Pi.**"

**Your Slide 6:** ❌ **Mentions physical hardware but NO instruction to hold devices to camera**

**Should Include:**
- Note: "(HOLD UP physical Arduino + PIR sensor to camera)"
- Text: "Here are the physical components you'll use in lab"
- Mention: "This demonstrates **hands-on pedagogy**, a key aspect of computing education"

---

## 🎯 STRUCTURE & FLOW ANALYSIS

### **Current Structure:**
1. Title
2. Learning Objectives
3. What is IoT?
4. The Challenge
5. Circuit Blueprint → **[SWITCH TO TINKERCAD]**
6. Summary

**Problems:**
1. ❌ **No clear "STOP SLIDES, START DEMO" indicator on Slide 5**
2. ❌ **No timing guidance** - You have 15 min total, 5-6 min demo
3. ❌ **No speaker notes** - How will you remember the "think aloud" script?

**Supervisor's Requirement:**
> "The slide should just be to show us the shock job, what you plan to do, and then **immediately jump to the practicals**"

**Your flow:** ✅ Structure is correct  
**Your execution:** ❌ Missing critical elements

---

### **Timing Breakdown (What You SHOULD Have):**

| Section | Time | Your Current Status |
|---------|------|---------------------|
| Slides 1-2 | 1.5 min | ⚠️ No timing notes |
| Slide 3 (IoT Definition) | 2 min | ⚠️ No timing notes |
| Slide 4 (Scenario) | 2 min | ⚠️ No timing notes |
| Slide 5 (Circuit) | 1 min | ⚠️ No timing notes |
| **TINKERCAD DEMO** | **5-7 min** | ❌ **No demo script in notes** |
| Physical Transition | 1 min | ❌ **NOT mentioned** |
| Slide 6 (Summary) | 2 min | ⚠️ No timing notes |
| **TOTAL** | **~15 min** | ❌ **Untrackable** |

**Impact:** You'll either run over time or finish too early

---

## 🎨 DESIGN PROBLEMS

### **1. Dark Background (#01404f) - WRONG CHOICE**

**Why It's Bad:**
- Hard to read white text on dark teal
- Depressing, not engaging
- Not appropriate for hands-on workshop feel

**Your PhD Viva:** Used dark backgrounds effectively with good contrast  
**Current:** Dark background makes everything hard to read

**Better Options:**
- White background with colored accents
- OR lighter background (#f5f5f5) with dark text
- OR keep dark but increase contrast (pure white text, larger fonts)

---

### **2. Emoji Overload - UNPROFESSIONAL**

**Current Emojis:**
- 🎯 (Learning Objectives)
- 🌐 (What is IoT)
- 👁️ 📡 🧠 (Components)
- 🚀 (Problem - wrong emoji!)
- ⚡ (Circuit)
- 📝 (Summary)

**Impact:** Looks like a middle school presentation, not university-level teaching

**Your PhD Viva (goodluckoguzie.github.io/Viva/):**
- ✅ ZERO emojis on main slides
- ✅ Professional icons and diagrams
- ✅ Clean, academic appearance

**Why the contrast?**
- PhD viva: Professional audience, academic context
- Current: Also professional audience (job interview panel!), but you're treating it casually

---

### **3. Font Choice - Ubuntu (Inconsistent)**

**Current:** Ubuntu font  
**Your PhD Viva:** Ubuntu font  
**Problem:** ❌ **You're copying your PhD viva style for a DIFFERENT PURPOSE**

**Why This Matters:**
- PhD viva = Research presentation (formal, academic)
- Micro-teach = Teaching demonstration (engaging, accessible)
- Different contexts require different designs

---

## 📝 MISSING SPEAKER NOTES - CRITICAL ERROR

**Current Status:** ❌ **NO SPEAKER NOTES AT ALL**

**Impact:**
- You'll forget the "think aloud" script
- You'll miss engagement questions
- You won't know when to hold up physical devices
- **You'll fail the interactive requirement**

**Supervisor's Requirement:**
> "**you should think aloud, engage with the audience**... making sure your audience so that you're not just one way"

**Your `MicroTeach_Script.md` exists** (98 lines of excellent content!)  
**Your presentation:** ❌ **Script NOT embedded in speaker notes**

**Example of What's Missing (from your script):**

**Slide 5 SHOULD have notes like:**
```html
<aside class="notes">
  [Time: 1 minute, then switch to Tinkercad]
  
  "Now let's look at our circuit blueprint."
  (Show slide, explain components)
  
  "Now I'm going to switch to Tinkercad and we'll build this together."
  
  [STOP SHARING SLIDES]
  [SHARE TINKERCAD BROWSER]
  
  Demo Script (5-7 minutes):
  - "Okay class, today we are building the core of a Smart Home Security system..."
  - "First, we need our 'eyes'. I am placing this PIR Motion Sensor."
  - Q: "Does anyone know what PIR stands for?"
  - A: "Passive Infrared - it detects heat energy, like body heat."
  ...
</aside>
```

**Current:** ❌ **COMPLETELY MISSING**

---

## 🤔 PEDAGOGY & TEACHING APPROACH

### **Supervisor's Key Phrases You MUST Include:**

From transcription:

1. **"Hands-on pedagogy"**
   - Current mention: ❌ None
   - Should be: Slide 6, when discussing physical hardware

2. **"Think aloud"**
   - Current implementation: ❌ No notes showing this
   - Should be: Speaker notes with thought process

3. **"Engage the audience" / "Interactive questioning"**
   - Current questions on slides: ❌ None visible
   - Should be: Visible prompts on Slides 3, 4, 5

4. **"Physical transition" (Simulation → Physical)**
   - Current implementation: ❌ Not explicitly shown
   - Should be: Slide 6 with camera instruction

---

### **The "Birmingham Constraint" - NOT ADDRESSED**

**Supervisor Mentioned:**
> "QAHE doesn't have dedicated lamps... **some classrooms that would become lamps**"

**Relevance to Your Presentation:**
- Students will do Tinkercad simulation first (safe, accessible)
- Then physical build in "computing labs" (shared classrooms)
- You should mention: "In our next lab session, in the computing lab, we'll build this physically"

**Current:** ❌ Just says "next session" - not specific enough

---

## 🎭 COMPARISON TO YOUR PhD VIVA

### **What Your PhD Viva Did RIGHT:**

Your PhD viva (https://goodluckoguzie.github.io/Viva/) is **EXCELLENT**:
- ✅ Clean, professional design
- ✅ Clear visual hierarchy
- ✅ Proper use of space
- ✅ No emojis (professional icons/diagrams)
- ✅ Consistent branding
- ✅ Academic credibility

### **What Your Current IoT Presentation Does WRONG:**

**You're trying to copy your PhD viva style, but:**
1. ❌ Different audience (academics vs. employers)
2. ❌ Different purpose (defend research vs. demonstrate teaching)
3. ❌ Different tone needed (formal vs. engaging)
4. ❌ Broke all the working links (dist/reveal.css doesn't exist)
5. ❌ Left placeholder content (Tinkercad screenshot)
6. ❌ Added childish elements (emoji overload)

**Result:** You took an A+ presentation and turned it into a D- presentation

---

## 💬 ENGAGEMENT QUESTIONS - COMPLETELY MISSING

**Supervisor's Explicit Requirement:**
> "Use those type of **prompting questions** that are easy to answer, but to get us to **participate**. So that you're not just doing it and we're watching"

**Your MicroTeach_Script.md has EXCELLENT questions:**
- "Does anyone know what PIR stands for?"
- "Why do I need this Resistor here?"
- "If we want to detect a burglar entering a room, what kind of sensor do you think we need?"

**Your Presentation Slides:** ❌ **ZERO questions visible**

**Impact:** Panel won't know you planned to engage them

**Fix:** Add questions to slides as visible prompts:
- **Slide 3:** "Q: What IoT devices do you use daily?"
- **Slide 4:** "Q: What sensor detects body heat?"
- **Slide 5:** "Q: Why do we need a resistor with the LED?"

---

## 🔧 TECHNICAL ISSUES THAT WILL BREAK YOUR PRESENTATION

### **Broken Reference #1: Missing dist/ folder**
```html
<link rel="stylesheet" href="dist/reset.css" />
<link rel="stylesheet" href="dist/reveal.css" />
```
**Impact:** ❌ **Presentation won't load**

### **Broken Reference #2: Missing mycss.css**
```html
<link rel="stylesheet" href="mycss.css" />
```
**Impact:** ❌ **Custom styles won't apply**

### **Broken Reference #3: Referencing plugin/ files locally**
```html
<script src="plugin/notes/notes.js"></script>
<script src="plugin/markdown/markdown.js"></script>
```
**Impact:** ❌ **Speaker notes and features won't work**

**During Interview:**
- You click to start presentation
- **Blank screen or unstyled mess**
- 5 minutes wasted troubleshooting
- Panel's first impression: "unprepared"
- **Automatic failure**

---

## 🎬 THE "PHYSICAL TRANSITION" MOMENT - MISSING

**Supervisor's EXACT requirement (most emphasized part of conversation):**

> "**[STOP SCREEN SHARE → TURN ON CAMERA]**
>
> 'So that logic works perfectly in code. But in the real world, we deal with physical constraints. **(Hold up your real Arduino and white PIR sensor)**
>
> Here is the physical version of that exact circuit. In our next lab, you will wire this yourself. You'll learn that real sensors have 'sensitivity' dials we need to adjust with a screwdriver, something the simulator doesn't always show us. **That is why Hands-On skills are critical**'"

**Your Presentation:** ❌ **NO MENTION of holding devices to camera**

**Impact:** **Fails the most emphasized requirement**

---

## 📊 FINAL GRADING BREAKDOWN

| Aspect | Weight | Grade | Score |
|--------|--------|-------|-------|
| **Slide Count (5-6 slides)** | 10% | A | 10/10 |
| **Content Accuracy** | 15% | B | 12/15 |
| **Visual Design** | 15% | D | 7/15 |
| **Engagement Elements** | 20% | F | 0/20 |
| **Speaker Notes** | 15% | F | 0/15 |
| **Technical Functionality** | 10% | F | 0/10 |
| **Pedagogy Alignment** | 15% | D | 6/15 |
| **Overall Professionalism** | | | |

**TOTAL: 35/100 (F - Failure)**

---

## 🚨 INTERVIEW KILLER CHECKLIST

**These issues will cause IMMEDIATE FAILURE:**

- [ ] ❌ **Broken links** - Presentation won't load
- [ ] ❌ **Placeholder content** - "(Paste Tinkercad Screenshot Here)"
- [ ] ❌ **Wrong title** - "PhD Viva Presentation"
- [ ] ❌ **Wrong date** - "December 2025" (future!)
- [ ] ❌ **No speaker notes** - Can't remember script
- [ ] ❌ **No engagement questions** - One-way presentation
- [ ] ❌ **No physical transition** - Missing key requirement
- [ ] ❌ **No "hands-on pedagogy" mention** - Supervisor's key phrase

---

## ✅ WHAT YOU MUST FIX (Priority Order)

### **Priority 1: CRITICAL (Must Fix or Fail)**

1. **Fix broken links**
   - Replace `dist/reveal.css` with CDN links
   - Remove reference to non-existent `mycss.css`
   
2. **Add Tinkercad circuit screenshot**
   - Build circuit in Tinkercad
   - Take screenshot
   - Replace placeholder

3. **Embed speaker notes**
   - Copy content from `MicroTeach_Script.md`
   - Add to `<aside class="notes">` in each slide
   - Include timing and "think aloud" prompts

4. **Fix title and metadata**
   - Change "PhD Viva" to "IoT Micro-Teach"
   - Fix date (2025 → 2024)
   - Verify email address

5. **Add physical transition to Slide 6**
   - Note: "(HOLD UP Arduino + PIR sensor to camera)"
   - Mention "hands-on pedagogy"

### **Priority 2: HIGH (Strongly Recommended)**

6. **Add engagement questions to slides**
   - Slide 3: Visible question prompt
   - Slide 4: Visible question prompt
   - Slide 5: Visible question prompt

7. **Replace emojis with professional visuals**
   - Real IoT device images
   - Circuit diagrams
   - Icons instead of emojis

8. **Add timing indicators**
   - Speaker notes with time per slide
   - Visual indicator: "SWITCH TO TINKERCAD" on Slide 5

### **Priority 3: MODERATE (Improve Quality)**

9. **Lighten background or increase contrast**
   - Current #01404f is too dark
   - White text hard to read

10. **Add visual flow diagram to Slide 4**
    - Not just text: INPUT → PROCESS → OUTPUT
    - Actual diagram with images

---

## 🎯 RECOMMENDED COMPLETE REDESIGN

**Based on supervisor requirements and your PhD viva quality:**

**Keep:**
- ✅ 6-slide structure
- ✅ Content accuracy
- ✅ Learning objectives

**Change:**
- ❌ Dark backgrounds → Light backgrounds or high contrast
- ❌ Emojis → Professional images/icons
- ❌ Missing elements → Add all required content
- ❌ PhD viva style → Teaching demonstration style

**Add:**
- ➕ Speaker notes from MicroTeach_Script.md
- ➕ Tinkercad screenshot
- ➕ Engagement questions (visible on slides)
- ➕ Physical transition moment
- ➕ Timing guidance
- ➕ "Hands-on pedagogy" mention

---

## 📝 SUPERVISOR'S UNSPOKEN EXPECTATIONS

### **What the Supervisor is REALLY Testing:**

1. **Can you follow instructions?**
   - 5-6 slides (✅ you did)
   - Include practical demo (⚠️ no script embedded)
   - Engage audience (❌ no questions visible)

2. **Do you understand pedagogy?**
   - "Hands-on" approach (❌ not mentioned)
   - "Think aloud" method (❌ not in notes)
   - Interactive teaching (❌ no questions)

3. **Are you prepared?**
   - Working presentation (❌ broken links)
   - Complete content (❌ placeholder screenshot)
   - Professional appearance (❌ wrong title)

4. **Can you bridge theory and practice?**
   - Simulation → Physical (⚠️ mentioned but not executed)
   - Explanation → Demonstration (⚠️ structure correct, execution weak)

**Current Score:** 2/4 (Failing)

---

## 💡 COMPARISON TO SUPERVISOR'S EXAMPLE

**Supervisor's Suggested Flow:**
1. Quick slides (5-6) showing plan
2. Jump to Tinkercad
3. **"Think aloud" while building**
4. Ask engagement questions during demo
5. **Hold up physical devices to camera**
6. Explain "hands-on pedagogy"
7. Summary slide

**Your Current Flow:**
1. ✅ 6 slides (good)
2. ⚠️ Slide 5 says switch to Tinkercad (ok)
3. ❌ No embedded demo script
4. ❌ No engagement questions visible
5. ❌ No camera instruction
6. ❌ No pedagogy mention
7. ✅ Summary slide exists (good)

**Alignment:** 40% (Failing)

---

## 🎓 WHAT YOUR PhD VIVA TEACHES US

**Your PhD viva is excellent because:**
- Clear structure
- Professional design
- Complete content
- Works perfectly

**Your IoT presentation fails because:**
- Copied PhD viva structure without adapting to new context
- Broke functional elements (CDN links → local files that don't exist)
- Added unprofessional elements (emoji overload)
- Left incomplete (placeholder content)

**Lesson:** ✅ **Professional ≠ Copying Your Previous Work**

**You need to:**
- Understand the different context (research vs. teaching)
- Adapt style accordingly (formal vs. engaging)
- Complete all elements (no placeholders)
- Test it works (check links)

---

## 🔥 FINAL VERDICT

**Current Presentation Grade: D- (35/100)**

**Will You Pass the Interview with This?** ❌ **NO**

**Why?**
1. Presentation likely won't load (broken links)
2. Placeholder content shows you're unprepared
3. Missing speaker notes = forgetting key points
4. No engagement = failing interactive requirement
5. No physical transition = missing most emphasized point

**Can It Be Fixed?** ✅ **YES - with significant work (3-4 hours)**

**Priority fixes:**
1. Fix all technical issues (broken links)
2. Add Tinkercad screenshot
3. Embed speaker notes
4. Add engagement questions
5. Add physical transition moment
6. Test thoroughly

**Time to Interview:** Unknown  
**Estimated Fix Time:** 3-4 hours  
**Recommendation:** **Fix immediately**

---

## 📞 QUESTIONS THE PANEL WILL ASK (From Transcription)

**Be prepared to answer:**

1. **"What's the difference between Arduino and Raspberry Pi?"**
   - Your answer should show you understand:
     - Arduino = Microcontroller (simple, real-time, low power)
     - Raspberry Pi = Mini-computer (complex, OS, more processing)
     - When to use each

2. **"Why did you choose Arduino for this project?"**
   - Answer: Simple, real-time sensor reading, perfect for beginners

3. **"If this was a 4-hour session, how would you structure it?"**
   - Be ready with: Theory (30 min) → Simulation (1 hr) → Physical build (2 hrs) → Testing (30 min)

4. **"What level is this targeted at?"**
   - Answer: Level 4-6 HE (Foundation to Year 2)

5. **"How do you ensure students don't damage equipment?"**
   - Answer: Safety training, supervision, checklists

**Current Preparation:** ❌ **No notes or preparation visible**

---

**Bottom Line:** Your current presentation would **fail the interview**. Fix the critical issues immediately, then test everything works. You have the knowledge (MicroTeach_Script.md is excellent), but the presentation doesn't demonstrate it.

**Next Steps:**
1. Read this entire document
2. Fix Priority 1 issues (critical)
3. Test presentation loads and works
4. Practice with timer (15 minutes total)
5. Prepare answers to panel questions

**Good luck - you'll need it if you present this version.**
