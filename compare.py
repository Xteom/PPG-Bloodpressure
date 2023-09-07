
def extract_episodes(candidates):
	"""
		Extracts the episodes from the raw data


		This function is likely to take 3-4 days to run on a Intel Core i7-7700 CPU
	"""

	try:								# making the necessary directories
		os.makedirs('ppgs')
	except Exception as e:
		print(e)

	try:
		os.makedirs('abps')
	except Exception as e:
		print(e)

	for k in tqdm(range(1,5), desc='Reading from Files'):				# iterating throug the files

		f = h5py.File('./raw_data/Part_{}.mat'.format(k), 'r')

		fs = 125																# sampling frequency
		t = 10																	# length of ppg episodes			
		samples_in_episode = round(fs * t)										# number of samples in an episode
		ky = 'Part_' + str(k)													# key

		for indix in tqdm(range(len(candidates)), desc='Reading from File {}/4'.format(k)):		# iterating through the candidates

			if(candidates[indix][0] != k):					# this candidate is from a different file
				continue

			record_no = int(candidates[indix][1])			# record no of the episode
			episode_st = int(candidates[indix][2])			# start of that episode

			ppg = []										# ppg signal
			abp = []										# abp signal

			for j in tqdm(range(episode_st, episode_st+samples_in_episode), desc='Reading Episode Id {}'.format(indix)):	

				ppg.append(f[f[ky][record_no][0]][j][0])	# ppg signal
				abp.append(f[f[ky][record_no][0]][j][1])	# abp signal

			pickle.dump(np.array(ppg), open(os.path.join('ppgs', '{}.p'.format(indix)), 'wb'))		# saving the ppg signal
			pickle.dump(np.array(abp), open(os.path.join('abps', '{}.p'.format(indix)), 'wb'))		# saving the abp signal

