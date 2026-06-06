# GYRA All UI

Single-file theme source for the GYRA desktop shell.

This file defines the complete visual direction and ready-to-place config blocks
for the GYRA theme pass: GTK, XFWM, XFCE session settings, Polybar, Alacritty,
LightDM, and GRUB.

## What This File Does

- Establishes one original GYRA desktop palette.
- Defines the window, panel, terminal, login, and boot appearance.
- Keeps the system minimal, dark, geometric, and steel-toned.
- Lists every external dependency that must exist outside this file.
- Provides config blocks that can be split into the target Linux paths.

## Visual Contract

GYRA should feel quiet, exact, and deliberate. The UI should sit behind the work,
not perform for attention.

Core rules:

- Dark steel surfaces.
- Low contrast borders.
- Sharp or lightly squared edges.
- No neon accents.
- No warm theme dominance.
- No theatrical security imagery in UI chrome.
- Text should stay readable without glowing.
- Functional elements should be compact and consistent.

## Palette

```ini
gyra-bg-0      = #0E0E0E
gyra-bg-1      = #111111
gyra-bg-2      = #171717
gyra-bg-3      = #1D1D1D
gyra-surface   = #151515
gyra-surface-2 = #202020
gyra-border    = #2A2A2A
gyra-border-hi = #3A3A3A
gyra-fg        = #C8C8C8
gyra-fg-strong = #E2E2E2
gyra-fg-muted  = #777777
gyra-fg-dim    = #555555
gyra-accent    = #ADADAD
gyra-accent-hi = #D0D0D0
gyra-danger    = #BF616A
gyra-warning   = #B9A36A
gyra-shadow    = #000000
```

## External Dependencies

These are intentionally not embedded in this file:

- `Iosevka Nerd Font` for Polybar and terminal symbols.
- `JetBrains Mono Nerd Font` as terminal fallback.
- `Noto Sans` for GTK, LightDM, and general UI.
- `Polybar`.
- `Alacritty`.
- `XFCE` with `xfwm4`.
- `LightDM GTK Greeter`.
- `GRUB` with `gfxterm` support.
- Desktop wallpaper: `/usr/share/gyra/backgrounds/oppex-agent-v1.jpg`.
- Lock screen artwork: `/usr/share/gyra/backgrounds/gyra-metal-badge.png`.
- Boot artwork: `/usr/share/gyra/grub/gyra-boot-badge.png`.
- UI mark: `/usr/share/gyra/icons/gyra-mark-light.svg`.
- Optional tray icon theme: a neutral monochrome icon theme, or a custom
  `Gyra-Steel` icon theme once assets exist.

## Install Map

```text
~/.themes/Gyra-Steel/index.theme
~/.themes/Gyra-Steel/gtk-3.0/gtk.css
~/.themes/Gyra-Steel/gtk-4.0/gtk.css
~/.themes/Gyra-Steel/xfwm4/themerc
~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
~/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml
~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
~/.config/polybar/config.ini
~/.config/polybar/scripts/window-tabs.sh
~/.config/alacritty/alacritty.toml
/etc/lightdm/lightdm-gtk-greeter.conf
/boot/grub/themes/gyra/theme.txt
```

## Metatheme

Target path:
`~/.themes/Gyra-Steel/index.theme`

```ini
[Desktop Entry]
Type=X-GNOME-Metatheme
Name=Gyra-Steel
Comment=GYRA steel desktop theme
Encoding=UTF-8

[X-GNOME-Metatheme]
GtkTheme=Gyra-Steel
MetacityTheme=Gyra-Steel
IconTheme=Adwaita
CursorTheme=Adwaita
ButtonLayout=:minimize,maximize,close
```

## GTK 3 Theme

Target path:
`~/.themes/Gyra-Steel/gtk-3.0/gtk.css`

```css
@define-color gyra_bg_0 #0E0E0E;
@define-color gyra_bg_1 #111111;
@define-color gyra_bg_2 #171717;
@define-color gyra_surface #151515;
@define-color gyra_surface_2 #202020;
@define-color gyra_border #2A2A2A;
@define-color gyra_border_hi #3A3A3A;
@define-color gyra_fg #C8C8C8;
@define-color gyra_fg_strong #E2E2E2;
@define-color gyra_fg_muted #777777;
@define-color gyra_fg_dim #555555;
@define-color gyra_accent #ADADAD;
@define-color gyra_accent_hi #D0D0D0;
@define-color gyra_danger #BF616A;
@define-color gyra_warning #B9A36A;

* {
  -gtk-icon-style: symbolic;
  -gtk-outline-radius: 0;
  outline-color: alpha(@gyra_accent, 0.22);
  outline-style: solid;
  outline-width: 1px;
  -gtk-secondary-caret-color: @gyra_accent;
}

window,
dialog,
popover,
menu,
.background {
  background-color: @gyra_bg_1;
  color: @gyra_fg;
}

window,
dialog {
  box-shadow: 0 18px 48px alpha(black, 0.38);
}

headerbar,
.titlebar {
  min-height: 28px;
  padding: 0 8px;
  background: @gyra_surface;
  border-bottom: 1px solid @gyra_border;
  color: @gyra_fg;
  box-shadow: none;
}

headerbar:backdrop,
.titlebar:backdrop {
  background: @gyra_bg_1;
  color: @gyra_fg_dim;
  border-bottom-color: alpha(@gyra_border, 0.65);
}

button {
  min-height: 24px;
  min-width: 24px;
  padding: 4px 10px;
  border-radius: 2px;
  border: 1px solid @gyra_border;
  background: @gyra_surface_2;
  color: @gyra_fg;
  box-shadow: none;
  text-shadow: none;
}

button:hover {
  border-color: @gyra_border_hi;
  background: #242424;
  color: @gyra_fg_strong;
}

button:active,
button:checked {
  background: #2B2B2B;
  border-color: @gyra_accent;
  color: @gyra_fg_strong;
}

button:disabled {
  background: @gyra_surface;
  border-color: alpha(@gyra_border, 0.55);
  color: @gyra_fg_dim;
}

entry,
spinbutton,
combobox box,
textview,
treeview,
list,
iconview {
  background-color: @gyra_bg_0;
  color: @gyra_fg;
  border: 1px solid @gyra_border;
  border-radius: 2px;
  selection-background-color: @gyra_accent;
  selection-color: @gyra_bg_0;
}

entry {
  min-height: 26px;
  padding: 4px 8px;
}

entry:focus,
textview:focus,
treeview:focus {
  border-color: @gyra_accent;
  box-shadow: inset 0 0 0 1px alpha(@gyra_accent, 0.35);
}

selection,
*:selected {
  background-color: @gyra_accent;
  color: @gyra_bg_0;
}

label:disabled,
*:disabled {
  color: @gyra_fg_dim;
}

notebook > header {
  background: @gyra_bg_1;
  border-color: @gyra_border;
}

notebook tab {
  min-height: 26px;
  padding: 4px 12px;
  background: @gyra_surface;
  border: 1px solid transparent;
  color: @gyra_fg_muted;
}

notebook tab:hover {
  color: @gyra_fg;
}

notebook tab:checked {
  background: @gyra_bg_0;
  border-color: @gyra_border;
  color: @gyra_fg_strong;
  box-shadow: inset 0 -2px @gyra_accent;
}

scrollbar {
  background: transparent;
  border: none;
}

scrollbar slider {
  min-width: 6px;
  min-height: 6px;
  border-radius: 0;
  background: #3A3A3A;
}

scrollbar slider:hover {
  background: @gyra_accent;
}

progressbar trough,
scale trough {
  min-height: 4px;
  background: @gyra_bg_0;
  border: 1px solid @gyra_border;
  border-radius: 0;
}

progressbar progress,
scale highlight {
  background: @gyra_accent;
  border-radius: 0;
}

switch {
  min-width: 42px;
  min-height: 22px;
  border-radius: 2px;
  background: @gyra_bg_0;
  border: 1px solid @gyra_border;
}

switch slider {
  min-width: 18px;
  min-height: 18px;
  margin: 1px;
  border-radius: 1px;
  background: @gyra_fg_muted;
}

switch:checked {
  background: #262626;
  border-color: @gyra_accent;
}

switch:checked slider {
  background: @gyra_accent_hi;
}

menu,
.menu,
popover {
  padding: 4px;
  background: @gyra_surface;
  border: 1px solid @gyra_border;
  border-radius: 2px;
}

menuitem,
modelbutton {
  min-height: 24px;
  padding: 5px 8px;
  color: @gyra_fg;
  border-radius: 1px;
}

menuitem:hover,
modelbutton:hover {
  background: @gyra_surface_2;
  color: @gyra_fg_strong;
}

separator {
  min-height: 1px;
  background: @gyra_border;
}

infobar.info,
infobar.question {
  background: #1B1B1B;
  color: @gyra_fg;
  border-bottom: 1px solid @gyra_border_hi;
}

infobar.warning {
  background: #211F18;
  color: @gyra_warning;
}

infobar.error {
  background: #241719;
  color: @gyra_danger;
}

.view {
  background: @gyra_bg_0;
  color: @gyra_fg;
}

.view:hover {
  background: #1A1A1A;
}

.view:selected {
  background: @gyra_accent;
  color: @gyra_bg_0;
}

.osd {
  background: alpha(#0E0E0E, 0.92);
  color: @gyra_fg;
  border: 1px solid @gyra_border_hi;
  border-radius: 2px;
}

.xfce4-panel {
  background: @gyra_bg_1;
  color: @gyra_fg;
}

.xfce4-panel button,
.xfce4-panel .tasklist button {
  min-height: 26px;
  min-width: 26px;
  padding: 0 8px;
  background: transparent;
  border: 0;
  border-radius: 0;
  color: @gyra_fg_muted;
}

.xfce4-panel button:hover {
  background: @gyra_surface;
  color: @gyra_fg;
}

.xfce4-panel button:checked,
.xfce4-panel .tasklist button:checked {
  background: @gyra_surface_2;
  box-shadow: inset 0 -2px @gyra_accent;
  color: @gyra_fg_strong;
}
```

## GTK 4 Theme

Target path:
`~/.themes/Gyra-Steel/gtk-4.0/gtk.css`

Use the same content as the GTK 3 file. GTK 4 supports the core selectors above
well enough for this first GYRA shell pass. Later, widget-specific GTK 4 tuning
can be split out after testing the actual installed apps.

## XFWM Theme

Target path:
`~/.themes/Gyra-Steel/xfwm4/themerc`

```ini
active_text_color=#E2E2E2
inactive_text_color=#555555
button_offset=1
button_spacing=3
show_app_icon=false
full_width_title=true
maximized_offset=0
title_horizontal_offset=0
title_shadow_active=false
title_shadow_inactive=false
title_vertical_offset_active=0
title_vertical_offset_inactive=0
shadow_delta_height=0
shadow_delta_width=0
shadow_delta_x=0
shadow_delta_y=-3
shadow_opacity=52
```

XFWM image asset intent:

```text
top-active.png              1px #151515 with 1px #2A2A2A lower edge
top-inactive.png            1px #111111 with 1px #1D1D1D lower edge
left-active.png             1px #202020
right-active.png            1px #202020
bottom-active.png           1px #202020
left-inactive.png           1px #151515
right-inactive.png          1px #151515
bottom-inactive.png         1px #151515
close-active.png            compact steel X glyph
hide-active.png             compact steel dash glyph
maximize-active.png         compact steel square glyph
*-inactive.png              same glyphs at #555555
*-prelight.png              same glyphs at #D0D0D0
*-pressed.png               same glyphs at #0E0E0E on #ADADAD
```

## XFCE Appearance Settings

Target path:
`~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml`

```xml
<?xml version="1.1" encoding="UTF-8"?>
<channel name="xsettings" version="1.0">
  <property name="Net" type="empty">
    <property name="ThemeName" type="string" value="Gyra-Steel"/>
    <property name="IconThemeName" type="string" value="Adwaita"/>
  </property>
  <property name="Xft" type="empty">
    <property name="HintStyle" type="string" value="hintslight"/>
    <property name="Hinting" type="int" value="1"/>
    <property name="RGBA" type="string" value="rgb"/>
    <property name="Antialias" type="int" value="1"/>
    <property name="DPI" type="int" value="96"/>
  </property>
  <property name="Gtk" type="empty">
    <property name="CursorThemeName" type="string" value="Adwaita"/>
    <property name="CursorThemeSize" type="int" value="24"/>
    <property name="FontName" type="string" value="Noto Sans 10"/>
    <property name="MonospaceFontName" type="string" value="Iosevka Nerd Font 10"/>
    <property name="ButtonImages" type="bool" value="false"/>
    <property name="MenuImages" type="bool" value="true"/>
    <property name="DecorationLayout" type="string" value=":minimize,maximize,close"/>
  </property>
  <property name="Xfce" type="empty">
    <property name="SyncThemes" type="bool" value="true"/>
  </property>
</channel>
```

## XFWM Runtime Settings

Target path:
`~/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml`

```xml
<?xml version="1.1" encoding="UTF-8"?>
<channel name="xfwm4" version="1.0">
  <property name="general" type="empty">
    <property name="theme" type="string" value="Gyra-Steel"/>
    <property name="title_font" type="string" value="Noto Sans 9"/>
    <property name="button_layout" type="string" value="O|HMC"/>
    <property name="activate_action" type="string" value="bring"/>
    <property name="box_move" type="bool" value="false"/>
    <property name="box_resize" type="bool" value="false"/>
    <property name="button_offset" type="int" value="0"/>
    <property name="button_spacing" type="int" value="0"/>
    <property name="click_to_focus" type="bool" value="true"/>
    <property name="cycle_preview" type="bool" value="true"/>
    <property name="double_click_action" type="string" value="maximize"/>
    <property name="focus_new" type="bool" value="true"/>
    <property name="frame_opacity" type="int" value="100"/>
    <property name="frame_border_top" type="int" value="0"/>
    <property name="full_width_title" type="bool" value="true"/>
    <property name="inactive_opacity" type="int" value="100"/>
    <property name="maximized_offset" type="int" value="0"/>
    <property name="placement_mode" type="string" value="center"/>
    <property name="placement_ratio" type="int" value="20"/>
    <property name="popup_opacity" type="int" value="100"/>
    <property name="raise_on_click" type="bool" value="true"/>
    <property name="resize_opacity" type="int" value="100"/>
    <property name="shadow_delta_height" type="int" value="0"/>
    <property name="shadow_delta_width" type="int" value="0"/>
    <property name="shadow_delta_x" type="int" value="0"/>
    <property name="shadow_delta_y" type="int" value="-3"/>
    <property name="shadow_opacity" type="int" value="52"/>
    <property name="show_app_icon" type="bool" value="false"/>
    <property name="show_dock_shadow" type="bool" value="true"/>
    <property name="show_frame_shadow" type="bool" value="true"/>
    <property name="show_popup_shadow" type="bool" value="false"/>
    <property name="snap_to_border" type="bool" value="true"/>
    <property name="snap_to_windows" type="bool" value="false"/>
    <property name="snap_width" type="int" value="10"/>
    <property name="tile_on_move" type="bool" value="true"/>
    <property name="title_alignment" type="string" value="center"/>
    <property name="title_horizontal_offset" type="int" value="0"/>
    <property name="title_shadow_active" type="string" value="false"/>
    <property name="title_shadow_inactive" type="string" value="false"/>
    <property name="title_vertical_offset_active" type="int" value="0"/>
    <property name="title_vertical_offset_inactive" type="int" value="0"/>
    <property name="use_compositing" type="bool" value="true"/>
    <property name="vblank_mode" type="string" value="auto"/>
    <property name="wrap_workspaces" type="bool" value="false"/>
  </property>
</channel>
```

## XFCE Desktop Settings

Target path:
`~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml`

```xml
<?xml version="1.1" encoding="UTF-8"?>
<channel name="xfce4-desktop" version="1.0">
  <property name="backdrop" type="empty">
    <property name="screen0" type="empty">
      <property name="monitor0" type="empty">
        <property name="color1" type="array">
          <value type="double" value="0.054901960784313725"/>
          <value type="double" value="0.054901960784313725"/>
          <value type="double" value="0.054901960784313725"/>
          <value type="double" value="1"/>
        </property>
        <property name="color-style" type="int" value="0"/>
        <property name="image-path" type="string" value="/usr/share/gyra/backgrounds/oppex-agent-v1.jpg"/>
        <property name="last-image" type="string" value="/usr/share/gyra/backgrounds/oppex-agent-v1.jpg"/>
        <property name="last-single-image" type="string" value="/usr/share/gyra/backgrounds/oppex-agent-v1.jpg"/>
        <property name="image-show" type="bool" value="true"/>
        <property name="image-style" type="int" value="5"/>
      </property>
    </property>
  </property>
  <property name="desktop-icons" type="empty">
    <property name="style" type="int" value="0"/>
    <property name="file-icons" type="empty">
      <property name="show-home" type="bool" value="false"/>
      <property name="show-filesystem" type="bool" value="false"/>
      <property name="show-removable" type="bool" value="false"/>
      <property name="show-trash" type="bool" value="false"/>
    </property>
    <property name="icon-size" type="uint" value="36"/>
    <property name="tooltip-size" type="double" value="48"/>
  </property>
</channel>
```

## Polybar

Target path:
`~/.config/polybar/config.ini`

```ini
[colors]
bg = #EE0E0E0E
bg-solid = #0E0E0E
surface = #151515
surface-2 = #202020
line = #2A2A2A
line-hi = #3A3A3A
fg = #C8C8C8
fg-strong = #E2E2E2
muted = #777777
dim = #555555
steel = #ADADAD
steel-hi = #D0D0D0
danger = #BF616A
warning = #B9A36A

[bar/gyra]
width = 100%
height = 34
radius = 0
fixed-center = true
bottom = false
background = ${colors.bg}
foreground = ${colors.fg}
line-size = 2
border-size = 0
padding-left = 1
padding-right = 1
module-margin = 0
separator =
font-0 = Iosevka Nerd Font:size=10;2
font-1 = Noto Sans:size=9;2
font-2 = Iosevka Nerd Font:size=13;3
modules-left = mark launcher files browser workspaces
modules-center = window-tabs
modules-right = network volume battery date power
cursor-click = pointer
enable-ipc = true
wm-restack = xfwm4
override-redirect = false
tray-position = right
tray-padding = 6
tray-maxsize = 18

[module/mark]
type = custom/text
content = G
content-font = 2
content-foreground = ${colors.fg-strong}
content-background = ${colors.surface}
content-padding = 2

[module/launcher]
type = custom/text
content = 󰆍
content-padding = 2
content-foreground = ${colors.muted}
click-left = rofi -show drun

[module/files]
type = custom/text
content = 󰉋
content-padding = 2
content-foreground = ${colors.muted}
click-left = thunar

[module/browser]
type = custom/text
content = 󰈹
content-padding = 2
content-foreground = ${colors.muted}
click-left = xdg-open about:blank

[module/workspaces]
type = internal/xworkspaces
pin-workspaces = true
enable-click = true
enable-scroll = false
format = <label-state>
label-active = %name%
label-active-padding = 3
label-active-background = ${colors.surface-2}
label-active-foreground = ${colors.fg-strong}
label-active-underline = ${colors.steel}
label-occupied = %name%
label-occupied-padding = 3
label-occupied-foreground = ${colors.muted}
label-empty = %name%
label-empty-padding = 3
label-empty-foreground = ${colors.dim}
label-urgent = %name%
label-urgent-padding = 3
label-urgent-background = ${colors.danger}
label-urgent-foreground = ${colors.bg-solid}

[module/window-tabs]
type = custom/script
exec = ~/.config/polybar/scripts/window-tabs.sh
tail = true
interval = 1
format-background = ${colors.bg}
format-foreground = ${colors.fg}

[module/network]
type = internal/network
interface-type = wired
interval = 2
format-connected = <label-connected>
format-disconnected = <label-disconnected>
label-connected = NET %downspeed%/%upspeed%
label-connected-padding = 2
label-connected-foreground = ${colors.muted}
label-disconnected = NET --
label-disconnected-padding = 2
label-disconnected-foreground = ${colors.dim}

[module/volume]
type = internal/pulseaudio
format-volume = <label-volume>
label-volume = VOL %percentage%%
label-volume-padding = 2
label-volume-foreground = ${colors.muted}
format-muted = <label-muted>
label-muted = VOL muted
label-muted-padding = 2
label-muted-foreground = ${colors.dim}

[module/battery]
type = internal/battery
battery = BAT0
adapter = AC
poll-interval = 5
format-charging = <label-charging>
format-discharging = <label-discharging>
format-full = <label-full>
label-charging = PWR %percentage%%
label-discharging = BAT %percentage%%
label-full = PWR full
label-charging-padding = 2
label-discharging-padding = 2
label-full-padding = 2
label-charging-foreground = ${colors.muted}
label-discharging-foreground = ${colors.muted}
label-full-foreground = ${colors.fg}

[module/date]
type = internal/date
interval = 1
date = %a %d %b
time = %H:%M
label = %date%  %time%
label-padding = 2
label-foreground = ${colors.fg}

[module/power]
type = custom/text
content = ⏻
content-padding = 2
content-foreground = ${colors.muted}
click-left = xfce4-session-logout
```

## Polybar Window Tabs Script

Target path:
`~/.config/polybar/scripts/window-tabs.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

active_id() {
  local dec
  dec="$(xdotool getactivewindow 2>/dev/null || true)"
  if [ -n "$dec" ]; then
    printf "0x%08x\n" "$dec"
  fi
}

print_tabs() {
  local active
  active="$(active_id)"

  wmctrl -lx 2>/dev/null | awk -v active="$active" '
    BEGIN {
      max = 28
    }
    {
      id = $1
      desktop = $2
      if (desktop == "-1") next
      title = ""
      for (i = 5; i <= NF; i++) {
        title = title (i == 5 ? "" : " ") $i
      }
      if (title == "") title = $3
      if (length(title) > max) title = substr(title, 1, max - 1) "..."

      if (tolower(id) == tolower(active)) {
        printf "%%{B#202020}%%{F#E2E2E2}  %s  %%{F-}%%{B-}", title
      } else {
        printf "%%{B#0E0E0E}%%{F#777777}  %s  %%{F-}%%{B-}", title
      }
    }
    END {
      printf "\n"
    }
  '
}

while true; do
  print_tabs
  sleep 1
done
```

Window tab dependencies:

- `wmctrl`
- `xdotool`

## Alacritty

Target path:
`~/.config/alacritty/alacritty.toml`

```toml
[window]
opacity = 0.96
padding = { x = 8, y = 6 }
dynamic_padding = false
decorations = "Full"

[font]
size = 10.5

[font.normal]
family = "Iosevka Nerd Font"
style = "Regular"

[font.bold]
family = "Iosevka Nerd Font"
style = "Bold"

[font.italic]
family = "Iosevka Nerd Font"
style = "Italic"

[cursor]
style = { shape = "Block", blinking = "Off" }
unfocused_hollow = true

[colors.primary]
background = "#0E0E0E"
foreground = "#C8C8C8"
dim_foreground = "#555555"
bright_foreground = "#E2E2E2"

[colors.cursor]
text = "#0E0E0E"
cursor = "#ADADAD"

[colors.selection]
text = "#0E0E0E"
background = "#ADADAD"

[colors.normal]
black = "#0E0E0E"
red = "#BF616A"
green = "#8F9A8A"
yellow = "#B9A36A"
blue = "#888888"
magenta = "#A0A0A0"
cyan = "#9CA6A6"
white = "#C8C8C8"

[colors.bright]
black = "#555555"
red = "#D0878E"
green = "#AAB4A5"
yellow = "#D0BE86"
blue = "#ADADAD"
magenta = "#C0C0C0"
cyan = "#B8C0C0"
white = "#E2E2E2"
```

## LightDM GTK Greeter

Target path:
`/etc/lightdm/lightdm-gtk-greeter.conf`

```ini
[greeter]
background = /usr/share/gyra/backgrounds/gyra-metal-badge.png
theme-name = Gyra-Steel
font-name = Noto Sans 10
icon-theme-name = Adwaita
xft-antialias = true
xft-dpi = 96
xft-hintstyle = slight
xft-rgba = rgb
indicators = ~host;~spacer;~session;~layout;~clock;~power;
clock-format = %d %b, %H:%M
screensaver-timeout = 60
default-user-image = /usr/share/gyra/icons/gyra-mark-light.svg
keyboard = onboard
position = 50%,center 50%,center
```

Greeter CSS intent:

```css
#panel_window {
  background: rgba(14, 14, 14, 0.94);
  color: #C8C8C8;
  border-bottom: 1px solid #2A2A2A;
}

#login_window {
  background: rgba(14, 14, 14, 0.86);
  border: 1px solid #2A2A2A;
  border-radius: 2px;
  box-shadow: 0 18px 48px rgba(0, 0, 0, 0.42);
}

#login_window entry {
  background: #0E0E0E;
  color: #C8C8C8;
  border: 1px solid #3A3A3A;
}

#login_window button {
  background: #202020;
  color: #C8C8C8;
  border: 1px solid #3A3A3A;
}
```

## GRUB Theme

Target path:
`/boot/grub/themes/gyra/theme.txt`

```ini
title-text: ""
desktop-image: "gyra-boot-badge.png"
desktop-color: "#0E0E0E"
terminal-font: "Iosevka Nerd Font Regular 16"
terminal-box: "terminal_*.png"
terminal-left: "0"
terminal-top: "0"
terminal-width: "100%"
terminal-height: "100%"

+ boot_menu {
  left = 34%
  top = 62%
  width = 32%
  height = 120
  item_font = "Iosevka Nerd Font Regular 14"
  item_color = "#777777"
  selected_item_color = "#E2E2E2"
  selected_item_pixmap_style = "select_*.png"
  item_height = 28
  item_padding = 6
  item_spacing = 4
}

+ label {
  left = 0
  top = 92%
  width = 100%
  height = 24
  align = "center"
  text = "GYRA"
  color = "#555555"
  font = "Noto Sans Regular 10"
}
```

GRUB asset intent:

```text
gyra-boot-badge.png     1920x1080, dark brushed metal badge centered
select_c.png            1px #202020 fill, 1px #ADADAD lower edge
terminal_*.png          transparent or #0E0E0E frame pieces
```

## First Boot Session Shape

Recommended first-boot desktop:

```text
Top bar:
  left: G mark, launcher, terminal, files, browser, workspaces
  center: live window tabs
  right: network, volume, battery, date, power

Desktop:
  no icons
  default wallpaper fills screen
  terminal opens centered at 92 columns x 28 rows

Window manager:
  near-invisible frame
  compact title bar
  no app icon in frame
  subtle shadow only

Terminal:
  dark steel background
  steel text
  compact padding
  no bright saturated prompt colors by default
```

## Originality Notes

- The palette is purpose-built for GYRA and uses only neutral steel tones plus
  restrained status colors.
- The GTK, Polybar, terminal, login, and boot blocks are newly written.
- The theme names, file paths, comments, metadata, and image dependencies are
  GYRA-specific.
- Existing external artwork must be supplied as GYRA assets at the paths listed
  above.
