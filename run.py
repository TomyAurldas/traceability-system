from src.parser import load_stories
from src.matrix_generator import generate_matrix
from src.report_generator import generate_report
from src.ci_runner import run_tests_and_generate_results

def main():
    # 🔥 Step 1: Run real CI (pytest)
    print("🔄 Running real CI (pytest)...")
    run_tests_and_generate_results()

    # Step 2: Load stories
    stories = load_stories()

    # ❌ REMOVE extract_test_ids (not needed anymore)

    # Step 3: Generate matrix (auto mapping used)
    df = generate_matrix(stories)

    # Step 4: Generate report
    generate_report(df)

    print("✅ Traceability report generated!")

if __name__ == "__main__":
    main()