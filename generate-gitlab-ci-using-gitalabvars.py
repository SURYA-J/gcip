from gcip import Pipeline, IncludeFile, Job

pipeline = Pipeline()
# Add include
gitlabci_include_file1 = {
    "file": "stacker-trunk-pipeline.yml",
    "project": "gitlab-ci/pipeline-templates/trunk/infra-stacker",
    "ref": "main"
}

gitlabci_include_file2 = {
    "file": ".gitlab-vars.yml",
    "project": "./"
}

include_file1 = IncludeFile(gitlabci_include_file1["file"], gitlabci_include_file1["project"], gitlabci_include_file1["ref"])
include_file2 = IncludeFile(gitlabci_include_file2["file"], gitlabci_include_file2["project"])

pipeline.add_include(include_file1)
pipeline.add_include(include_file2)

# Add variables
gitlabci_variables = {
    "CFN_LINT_IGNORE_CHECKS": "W3011,E3002,W1001"
}
pipeline.add_variables(**gitlabci_variables)

job1 = Job(stage="start", script="echo 'build'")
job2 = Job(stage="build", script="echo 'build'", variables={"testvar":"abcd"})
pipeline.add_children(job1, job2)

# Write to YAML
pipeline.write_yaml("gitlab-ci.yml")
