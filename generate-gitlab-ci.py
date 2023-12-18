from gcip import Pipeline, IncludeFile, Job

pipeline = Pipeline()
# Add include
gitlabci_include_file = {
    "file": "stacker-trunk-pipeline.yml",
    "project": "gitlab-ci/pipeline-templates/trunk/infra-stacker",
    "ref": "main"
}

include_file = IncludeFile(gitlabci_include_file["file"], gitlabci_include_file["project"], gitlabci_include_file["ref"])

pipeline.add_include(include_file)

# Add variables
gitlabci_variables = {
    "CFN_LINT_IGNORE_CHECKS": "W3011,E3002,W1001"
}
pipeline.add_variables(**gitlabci_variables)

job1 = Job(stage="start", script="echo 'start'")
job2 = Job(stage="build", script="echo 'build'", variables={"testvar":"abcd"})
pipeline.add_children(job1, job2)

# Write to YAML
pipeline.write_yaml("gitlab-ci.yml")
