# Cyclomatic Complexity Demo - REVISED Script (Green to Red)

## 🎯 Learning Objective
Demonstrate how **quality gates** protect code quality by showing a PASSING pipeline first (GREEN ✅), then introducing complex code that FAILS (RED ❌).

---

## 📚 What is Cyclomatic Complexity?

**Definition**: A software metric that measures the number of independent paths through a program's source code.

**Industry Standards**:
- **1-5**: ✅ Simple, low risk, easy to test
- **6-10**: ⚠️ Moderate complexity, acceptable
- **11-20**: ❌ Complex, high risk, hard to maintain
- **21+**: 🚨 Very high risk, UNMAINTAINABLE

---

## 🎬 Demo Script (Green → Red Approach)

### Step 1: Show the GOOD Code (GREEN ✅)

**What to Say**:
> "I've written a student grade calculator using best practices. Let me show you the code and then push it to see our quality gate in action."

**Show the Code**: Open `messy_logic.py` (current clean version)

**Key Points to Highlight**:
- ✅ **Three small functions** instead of one giant function
- ✅ **Single Responsibility**: Each function has one job
- ✅ **No deep nesting**: Simple, readable logic
- ✅ **Data-driven**: Uses weighted scoring and lookup tables

**What to Say**:
> "Notice how this is organized:
> - `calculate_student_grade()` - orchestrates the calculation
> - `calculate_total_points()` - handles the math
> - `get_letter_grade()` - converts points to grades
> 
> Each function is simple and focused. This is maintainable code."

---

### Step 2: Push and Show GREEN Pipeline ✅

**Actions**:
```bash
git add messy_logic.py .github/workflows/quality_gate.yml
git commit -m "Add student grade calculator with quality gate"
git push origin main
```

**What to Show**:
1. Navigate to GitHub → **Actions** tab
2. Click on the running workflow
3. Watch it **PASS** with a **green checkmark** ✅

**What to Say**:
> "The pipeline is running our complexity check with a threshold of 5. Let's see what happens..."

**Show the Success**:
Click into the successful job and show the **"Check Cyclomatic Complexity"** step.

**Expected Output**:
```
Running complexity check with max-complexity=5...
✅ No complexity violations found!
```

**Key Teaching Points**:
- ✅ **Quality Gate Passed**: Code meets our standards
- ✅ **Automated Verification**: No manual review needed for this metric
- ✅ **Complexity ≤ 5**: Each function is simple and maintainable
- ✅ **Ready to Merge**: This code is acceptable

---

### Step 3: Introduce the BAD Code (Prepare for RED ❌)

**What to Say**:
> "Now, let me show you what happens when someone writes complex, unmaintainable code. I'm going to refactor this into a single, deeply nested function."

**Actions**:
1. Open `messy_logic_BACKUP.py` (the complex version)
2. Show the nested if/else statements on screen
3. Scroll through the 15+ levels of nesting

**What to Say**:
> "Look at this version. It does the same thing, but it's all in ONE function with 15+ levels of nested if/else statements. This is a maintenance nightmare:
> - Hard to understand what it does
> - Difficult to test all the paths
> - Easy to introduce bugs
> - Impossible to modify safely
> 
> Let's see if our quality gate catches this..."

---

### Step 4: Replace with BAD Code and Push (RED ❌)

**Actions**:
```bash
# Copy the messy version over the clean version
cp messy_logic_BACKUP.py messy_logic.py

git add messy_logic.py
git commit -m "Refactor grade calculator into single function (BAD IDEA)"
git push origin main
```

**What to Show**:
1. Return to GitHub → **Actions** tab
2. Click on the new workflow run
3. Watch it **FAIL** with a **red X** ❌

**What to Say**:
> "The pipeline is running the same quality check. But this time..."

---

### Step 5: Explain the Failure (The Teaching Moment)

**Click into the failed job** and show the **"Check Cyclomatic Complexity"** step.

**Expected Error Output**:
```
messy_logic.py:13:1: C901 'calculate_student_grade' is too complex (33)
```

**What to Say**:
> "BOOM! The quality gate caught it. Let's break down this error:
> - **C901**: Flake8 error code for 'function is too complex'
> - **Line 13**: Where the problematic function starts
> - **Complexity 33**: The measured complexity (threshold was 5!)
> 
> Our quality gate rejected this code automatically. No human had to review it and say 'this looks complicated' - the metric is objective and measurable."

**Key Teaching Points**:
- ❌ **Safety Net in Action**: Bad code was blocked automatically
- ❌ **Objective Metric**: Not opinion - it's a number (33 vs 5)
- ❌ **33 Complexity** = 33+ independent code paths to test
- ❌ **Prevents Technical Debt**: Stops unmaintainable code before it enters the codebase

---

### Step 6: Compare the Two Versions (Side-by-Side)

**Show Both Files**:
- **Clean version** (complexity ~5): Three focused functions
- **Messy version** (complexity 33): One giant nested function

**What to Say**:
> "Same functionality, completely different complexity:
> 
> **Clean Version**:
> - Complexity: ~5 per function
> - Easy to test
> - Easy to modify
> - Easy to understand
> 
> **Messy Version**:
> - Complexity: 33
> - Dozens of test cases needed
> - Risky to modify
> - Hard to understand
> 
> This is why we enforce quality gates in our CI/CD pipeline."

---

## 📊 Visual Comparison

### GREEN Version (Passes ✅)
```
Function: calculate_student_grade()    Complexity: 3
Function: calculate_total_points()     Complexity: 1
Function: get_letter_grade()           Complexity: 1
-------------------------------------------
Total: 3 functions, max complexity: 3  ✅ PASS
```

### RED Version (Fails ❌)
```
Function: calculate_student_grade()    Complexity: 33
-------------------------------------------
Total: 1 function, max complexity: 33  ❌ FAIL
```

---

## 🎓 Discussion Questions

1. **Why did the first version pass?**
   - Small, focused functions
   - Each function has one responsibility
   - Low complexity (≤5)

2. **Why did the second version fail?**
   - One giant function doing everything
   - 33 decision points = 33+ code paths
   - Violates quality standards

3. **What's the benefit of automated quality gates?**
   - Catches issues immediately
   - Objective, not subjective
   - Prevents bad code from being merged
   - Enforces team standards consistently

4. **How would you fix the messy version?**
   - Extract helper functions
   - Use data structures (lookup tables)
   - Replace conditionals with calculations
   - Apply Single Responsibility Principle

---

## ✅ Key Takeaways

1. **Start with good code** to show what "right" looks like
2. **Quality gates enforce standards** automatically
3. **Complexity is measurable** - not just opinion
4. **Refactoring reduces complexity** and improves maintainability
5. **CI/CD pipelines protect quality** before code reaches production

---

## 🚀 Quick Reference Commands

### Push CLEAN version (GREEN ✅):
```bash
# messy_logic.py already has clean version
git add messy_logic.py .github/workflows/quality_gate.yml
git commit -m "Add grade calculator with quality gate"
git push origin main
```

### Push MESSY version (RED ❌):
```bash
cp messy_logic_BACKUP.py messy_logic.py
git add messy_logic.py
git commit -m "Refactor into single function (demonstrates high complexity)"
git push origin main
```

### Restore CLEAN version (GREEN ✅):
```bash
git revert HEAD
git push origin main
```

---

## 📝 Files in This Demo

1. **messy_logic.py** - Currently contains CLEAN version (complexity ~5)
2. **messy_logic_BACKUP.py** - Contains MESSY version (complexity 33)
3. **.github/workflows/quality_gate.yml** - Quality gate with threshold=5
4. **COMPLEXITY_DEMO_SCRIPT_REVISED.md** - This teaching script

**Demo Flow**: Clean (GREEN) → Messy (RED) → Discussion
