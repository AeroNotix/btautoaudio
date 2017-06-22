REMOTE_DEST?=
REMOTE_PATH?=

all:
	makepkg -sf
	scp *.xz ${REMOTE_DEST}:${REMOTE_PATH}
	ssh ${REMOTE_DEST} 'cd ${REMOTE_PATH} && sudo pacman -U --noconfirm *.xz'
