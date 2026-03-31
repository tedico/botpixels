# ClawdIcons

![Clawd](icons/clawd.svg)

A pixel-art icon set featuring the Claude Code mascot in various actions, states, and life scenarios.

All icons are built on the same base mascot from [Claude Code](https://docs.anthropic.com/en/docs/claude-code), with contextual indicators for different situations.

## Preview

Open `icons/preview.html` in a browser to see all icons, or check the grid below:

### Tools (10)

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Read](icons/clawd_read.svg) | ![Edit](icons/clawd_edit.svg) | ![Write](icons/clawd_write.svg) | ![Bash](icons/clawd_bash.svg) | ![Glob](icons/clawd_glob.svg) |
| Read | Edit | Write | Bash | Glob |
| ![Grep](icons/clawd_grep.svg) | ![LSP](icons/clawd_lsp.svg) | ![WebFetch](icons/clawd_webfetch.svg) | ![WebSearch](icons/clawd_websearch.svg) | ![Notebook](icons/clawd_notebook.svg) |
| Grep | LSP | WebFetch | WebSearch | Notebook |

### Dev Actions (21)

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Git](icons/clawd_git.svg) | ![Commit](icons/clawd_commit.svg) | ![Merge](icons/clawd_merge.svg) | ![PR](icons/clawd_pr.svg) | ![Diff](icons/clawd_diff.svg) |
| Git | Commit | Merge | PR | Diff |
| ![Debug](icons/clawd_debug.svg) | ![Test](icons/clawd_test.svg) | ![Build](icons/clawd_build.svg) | ![Deploy](icons/clawd_deploy.svg) | ![Install](icons/clawd_install.svg) |
| Debug | Test | Build | Deploy | Install |
| ![Lint](icons/clawd_lint.svg) | ![Review](icons/clawd_review.svg) | ![Curl](icons/clawd_curl.svg) | ![Docker](icons/clawd_docker.svg) | ![SSH](icons/clawd_ssh.svg) |
| Lint | Review | HTTP | Docker | SSH |
| ![DB](icons/clawd_db.svg) | ![API](icons/clawd_api.svg) | ![Log](icons/clawd_log.svg) | ![CI](icons/clawd_ci.svg) | ![Config](icons/clawd_config.svg) |
| Database | API | Logs | CI/CD | Config |
| ![Env](icons/clawd_env.svg) | | | | |
| Env Vars | | | | |

### States (12)

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Agent](icons/clawd_agent.svg) | ![Explore](icons/clawd_explore.svg) | ![Plan](icons/clawd_plan.svg) | ![Think](icons/clawd_think.svg) | ![Answer](icons/clawd_answer.svg) |
| Agent | Explore | Plan | Think | Answer |
| ![Ask](icons/clawd_ask.svg) | ![Wait](icons/clawd_wait.svg) | ![Error](icons/clawd_error.svg) | ![Success](icons/clawd_success.svg) | ![Confused](icons/clawd_confused.svg) |
| Ask | Wait | Error | Success | Confused |
| ![Eureka](icons/clawd_eureka.svg) | ![Focus](icons/clawd_focus.svg) | | | |
| Eureka | Focus | | | |

### Life (22)

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Rest](icons/clawd_rest.svg) | ![Run](icons/clawd_run.svg) | ![Sleep](icons/clawd_sleep.svg) | ![Drink](icons/clawd_drink.svg) | ![Eat](icons/clawd_eat.svg) |
| Rest | Run | Sleep | Drink | Eat |
| ![Coffee](icons/clawd_coffee.svg) | ![Happy](icons/clawd_happy.svg) | ![Sad](icons/clawd_sad.svg) | ![Music](icons/clawd_music.svg) | ![Game](icons/clawd_game.svg) |
| Coffee | Happy | Sad | Music | Game |
| ![Book](icons/clawd_read_book.svg) | ![Wave](icons/clawd_wave.svg) | ![Meditate](icons/clawd_meditate.svg) | ![Rain](icons/clawd_rain.svg) | ![Love](icons/clawd_love.svg) |
| Book | Wave | Meditate | Rain | Love |
| ![Workout](icons/clawd_workout.svg) | ![Cook](icons/clawd_cook.svg) | ![Travel](icons/clawd_travel.svg) | ![Photo](icons/clawd_photo.svg) | ![Dance](icons/clawd_dance.svg) |
| Workout | Cook | Travel | Photo | Dance |
| ![Pet](icons/clawd_pet.svg) | ![Birthday](icons/clawd_birthday.svg) | | | |
| Pet | Birthday | | | |

## Usage

Each icon is a standalone SVG file (128x128 viewBox). Use them directly:

```html
<img src="icons/clawd_think.svg" width="64" height="64" alt="Thinking">
```

## Regenerate

All icons are generated from a single Python script:

```bash
python3 generate_icons.py
```

## Structure

```
clawdary/
  clawd.svg              # Base mascot SVG
  generate_icons.py      # Icon generator script
  icons/
    clawd_*.svg          # 65 icon SVGs
    preview.html         # Visual preview page
```

## License

MIT
