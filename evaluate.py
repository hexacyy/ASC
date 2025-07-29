import pandas as pd
from detector import analyze_command
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


def normalize_label(label):
    """Map CSV labels into our expected format."""
    label = label.lower().strip()
    if label == "benign":
        return "legitimate"
    return label


def run_evaluation(csv_path, verbose=True):
    """
    Main evaluation function that returns metrics and optionally prints detailed results.
    
    Args:
        csv_path: Path to the CSV file
        verbose: If True, prints individual predictions; if False, only prints summary
    
    Returns:
        tuple: (accuracy, precision, recall, f1, correct_count, total_count)
    """
    df = pd.read_csv(csv_path).dropna(subset=["prompt", "Label"])
    
    y_true = []
    y_pred = []
    
    if verbose:
        print("=== Evaluating MalCommandGuard ===\n")
    
    for index, row in df.iterrows():
        cmd = row["prompt"]
        actual = normalize_label(row["Label"])
        predicted = analyze_command(cmd)["verdict"]
        
        y_true.append(actual)
        y_pred.append(predicted)
        
        if verbose:
            print(f"[{index+1}] CMD: {cmd}")
            print(f" → Predicted: {predicted.upper()} | Actual: {actual.upper()}\n")
    
    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
    
    correct_count = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    total_count = len(y_true)
    
    return accuracy, precision, recall, f1, correct_count, total_count


def print_summary_results(accuracy, precision, recall, f1, correct_count, total_count):
    """Print results in the desired summary format."""
    print(f"✅ Summary: Accuracy = {accuracy:.2%} ({correct_count}/{total_count} correct)")
    print()
    print("=== Detailed Metrics ===")
    print(f"Accuracy:  {accuracy:.2%}")
    print(f"Precision: {precision:.2%}")
    print(f"Recall:    {recall:.2%}")
    print(f"F1 Score:  {f1:.2%}")


def print_detailed_results(csv_path, y_true, y_pred):
    """Print detailed classification report and confusion matrix."""
    print("\n=== Classification Report ===")
    print(classification_report(y_true, y_pred, digits=3))
    
    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_true, y_pred))


def evaluate_model(csv_path, show_individual=False, show_detailed=False):
    """
    Main evaluation function with flexible output options.
    
    Args:
        csv_path: Path to the CSV file
        show_individual: If True, shows individual command predictions
        show_detailed: If True, shows classification report and confusion matrix
    
    Returns:
        dict: Dictionary with all metrics
    """
    # Run evaluation
    accuracy, precision, recall, f1, correct, total = run_evaluation(csv_path, verbose=show_individual)
    
    # Always show summary
    print_summary_results(accuracy, precision, recall, f1, correct, total)
    
    # Optionally show detailed metrics
    if show_detailed:
        # We need to re-run to get y_true and y_pred for detailed output
        df = pd.read_csv(csv_path).dropna(subset=["prompt", "Label"])
        y_true, y_pred = [], []
        
        for _, row in df.iterrows():
            actual = normalize_label(row["Label"])
            predicted = analyze_command(row["prompt"])["verdict"]
            y_true.append(actual)
            y_pred.append(predicted)
        
        print_detailed_results(csv_path, y_true, y_pred)
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'correct': correct,
        'total': total
    }


if __name__ == "__main__":
    # Example usage with different output options:
    
    # Option 1: Just summary (what you want)
    print("=== SUMMARY ONLY ===")
    evaluate_model("data/cmd_huge_known_commented_updated.csv")
    
    print("\n" + "="*60 + "\n")
    
    # Option 2: With individual predictions
    print("=== WITH INDIVIDUAL PREDICTIONS ===")
    evaluate_model("data/cmd_huge_known_commented_updated.csv", show_individual=True)
    
    print("\n" + "="*60 + "\n")
    
    # Option 3: With detailed metrics
    print("=== WITH DETAILED METRICS ===")
    evaluate_model("data/cmd_huge_known_commented_updated.csv", show_detailed=True)