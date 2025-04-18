import optuna
import optuna.visualization as vis

if __name__ == "__main__":
    study = optuna.create_study(
        study_name="CDEAgent-exhaustive",
        load_if_exists=True,
        storage="sqlite:///cde_agent.db",
    )

    importances = optuna.importance.get_param_importances(study)
    top_5 = list(sorted(importances.keys(), key=lambda param: importances[param]))[:4]
    fig = vis.plot_contour(study, params=top_5)
    fig.show()
    fig = vis.plot_slice(study)
    fig.show()

    for trial in study.best_trials:
        print("Trial number: ", trial.number)
        print("Value: ", trial.value)
        print("Params: ")
        for key, value in trial.params.items():
            print(f"  {key}: {value}")
        print("User attrs: ")
        for key, value in trial.user_attrs.items():
            print(f"  {key}: {value}")
        print()
